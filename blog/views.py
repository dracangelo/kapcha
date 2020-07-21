from django.shortcuts import render
from .models import Post, Category, Comment
from django.db.models import Q
from taggit.models import Tag
from django.core.paginator import Paginator
from .forms import CommentForm  


# Create your views here.

def list(request):
    list = Post.objects.all()

    #search 
    search_query = request.GET.get('q')
    if search_query :
        list = list.filter(
            Q(title__icontains = search_query)|
            Q(content__icontains= search_query) |
            Q(tags__name__icontains= search_query)
        ).distinct()
    
    #pagination
    paginator = Paginator(list, 2) # 2 post per page
    page = request.GET.get('page')

    list = paginator.get_page(page)
    
    context = {
        'list': list
    }

    return render(request, 'blog/blog.html', context)


def detail(request, id):

    detail = Post.objects.get(id=id)
    categories = Category.objects.all()
    all_tags = Tag.objects.all()
    comments = Comment.objects.filter(post=detail)
    

    if request.method == 'POST' :
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = detail
            new_comment.save()

    else:
        comment_form = CommentForm()

    context = {
        'detail' : detail ,
        'categories' : categories ,
        'all_tags' : all_tags ,
        'comments' : comments ,
        'comment_form' : comment_form
    }

    return render(request, 'blog/detail.html', context)


def category(request, category):
    category = Post.objects.filter(category__name=category)
    context = {
        'list' : category ,
    }

    return render(request , 'blog/blog.html' , context)



def tag(request , tag):
    tag = Post.objects.filter(tags__name__in=[tag])
    context = {
        'list' : tag ,
    }

    return render(request , 'blog/blog.html' , context)
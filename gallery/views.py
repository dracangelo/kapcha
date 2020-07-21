from django.shortcuts import render
from .models import Gallery
from taggit.models import Tag

# Create your views here.
def gallery(request):
    pic = Gallery.objects.all()
    all_tags = Tag.objects.all()

    context = {
        'pic': pic,
        'all_tags' : all_tags ,
    }

    return render (request, 'gallery/gallery.html', context)

def tag(request , tag):
    tag = Gallery.objects.filter(tags__name__in=[tag])
    context = {
        'pic' : tag ,
    }

    return render(request , 'gallery/gallery.html' , context)
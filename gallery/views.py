from django.shortcuts import render
from .models import Gallery

# Create your views here.
def gallery(request):
    pic = Gallery.objects.all()

    context = {
        'pic': pic
    }

    return render (request, 'gallery/gallery.html', context)

def tag(request , tag):
    tag = Gallery.objects.filter(tags__name__in=[tag])
    context = {
        'pic' : tag ,
    }

    return render(request , 'gallery/gallery.html' , context)
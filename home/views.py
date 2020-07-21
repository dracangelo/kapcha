from django.shortcuts import render
from gallery.models import Gallery

# Create your views here.

def home(request):
    home = Gallery.objects.all()

    context = {
        'home':home
    }

    return render(request, 'home/home.html', context)
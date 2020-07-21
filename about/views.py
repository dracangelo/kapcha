from django.shortcuts import render
from .models import About, Team

# Create your views here.

def aboutus(request):
    about = About.objects.last()
    team = Team.objects.all()

    context = {
        'about':about,
        'team':team
    }

    
    return render (request, 'about/about.html', context)
from . import views
from django.urls import path, include

app_name='about'

urlpatterns = [
    path('', views.aboutus, name='about'),
    
]
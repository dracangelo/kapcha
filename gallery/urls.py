from . import views
from django.urls import path, include

app_name='gallery'

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('tags=<slug:tag>', views.tag, name='tag'),
    
]
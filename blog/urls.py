from . import views
from django.urls import path, include

app_name='blog'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:id>', views.detail, name='detail'),
    path('category=<slug:category>', views.category, name='category'),
    path('tags=<slug:tag>', views.tag, name='tag'),
]
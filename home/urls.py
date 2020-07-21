from . import views
from django.urls import path, include

app_name='home'

urlpatterns = [
    path('', views.home, name='home'),
]
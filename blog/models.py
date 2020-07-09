from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager 

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

class Category(models.Model):
    name =  models.CharField(max_length=20)

    class Meta:
        verbose_name = 'CAtegory'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Comment(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        created = models.DateField(default=timezone.now)
        content = models.TextField()

        class Meta:
            verbose_name = 'Comment'
            verbose_name_plural = 'Comments'

        def __str__(self):
            return str(self.content)
from django.db import models
from taggit.managers import TaggableManager 

# Create your models here.

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length = 14)
    tags = TaggableManager(blank=True)


    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.title





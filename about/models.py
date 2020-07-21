from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()


    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.title

class Team(models.Model):
    image = models.ImageField(upload_to='team/')
    title = models.CharField(max_length=25)
    role = models.CharField(max_length=50)
    myself = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.title
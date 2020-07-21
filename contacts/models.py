from django.db import models

# Create your models here.


class Contact(models.Model):
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class Reserve(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    notes = models.TextField()

    def __str__(self):
        return self.name
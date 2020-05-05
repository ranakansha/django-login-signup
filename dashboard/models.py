from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name

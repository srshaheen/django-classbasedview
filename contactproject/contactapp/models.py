from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    cell = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

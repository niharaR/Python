from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=150)
    img=models.ImageField(upload_to='pics')

def __str__(self):
    return self.name
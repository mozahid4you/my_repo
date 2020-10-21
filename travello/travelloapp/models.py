from django.db import models


# Create your models here.
class Travellomodel(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to=('travelloimg'))
    description=models.TextField(max_length=200)
    def __str__(self):
        return self.title



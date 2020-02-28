from django.db import models


# Create your models here.
class Photo(models.Model):
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    date = models.DateField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

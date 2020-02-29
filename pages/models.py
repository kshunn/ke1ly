from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    date = models.DateField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

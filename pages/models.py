from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    date = models.DateField('date published')
    image = models.ImageField(upload_to="image", null=True)

    def __str__(self):
        return self.title

from turtle import onclick
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Links(models.Model):
    name = models.CharField(max_length=200)
    link = models.TextField()
    unique_code = models.CharField(max_length=10,unique= True)
    shorten_link = models.CharField(max_length=200)
    visits = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="links")


    def __str__(self):
        return self.name
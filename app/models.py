from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todolist(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank=True)
    title = models.CharField(max_length=255)
    days = models.IntegerField()
    is_completed = models.BooleanField()
    
    
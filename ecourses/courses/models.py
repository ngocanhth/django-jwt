from distutils.command.upload import upload
from pydoc import describe
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%n')
    
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    
class Course (models.Model):
    subject = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
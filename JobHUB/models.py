from django.conf import Settings
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import AbstractUser
# from .models import MyUser

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib.auth.models import AbstractUser

# class MyUser(AbstractUser):
#     is_student = models.BooleanField(default=False)
#     groups = models.ManyToManyField(
#         'auth.Group',
#         verbose_name='groups',
#         blank=True,
#         help_text='The groups this user belongs to.',
#         related_name='myuser_set',  # Add a related_name argument
#         related_query_name='user',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         verbose_name='user permissions',
#         blank=True,
#         help_text='Specific permissions for the user.',
#         related_name='myuser_set+',  # Update the related_name argument
#         related_query_name='user',
#     )

# from django.contrib.auth.models import User
# Create your models here.
def calculate_default_mobile():
    # Logic to calculate the default name
    return '1234455'
class registration(models.Model):
   
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    username=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    mobile=models.CharField(max_length=10,default=calculate_default_mobile)
    Highest_Qualification_choices = (
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('MCa','MCA'),
        ('BCA','BCA'),
        ('BSC','BSC'),
    )
    Highest_Qualification= models.CharField(max_length=10, choices=Highest_Qualification_choices,default="B.Tech")
  
    pdf_file=models.FileField(upload_to='documents/{Resume}/', default='default.pdf')
    
    def __str__(self):
        return self.first_name

class company_registration(models.Model):
    username=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    mobile=models.CharField(max_length=10,default=calculate_default_mobile)
    company_name=models.CharField(max_length=30)
    role=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.username
    
class jobcreate(models.Model):
    company=models.CharField(max_length=30,default="abc info tech",null=True, blank=True)
    experience =models.CharField(max_length=30,default="0-1yr exp")
    location=models.CharField(max_length=20,default="Hyderabad")
    username=models.CharField(max_length=20,default="James", null=True, blank=True)
    mobile=models.CharField(max_length=10,default=calculate_default_mobile)
    job_role= models.CharField(max_length=30,default="React developer", null=True, blank=True) 
    
    def __str__(self):
        return self.username
    
         


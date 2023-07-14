from django.db import models
from django import forms
from .models import registration
# Create your models here.
# class registrstion_form(models.ModelForm):
#     first_name=forms.CharField(max_length=20)
#     last_name=forms.CharField(max_length=20)
#     username=forms.CharField(max_length=10)
#     email=forms.EmailField()
#     mobile=forms.CharField(max_length=10)
#     password1=forms.CharField(max_length=10)
#     Highest_Qualification=forms.CharField(max_length=10)
#     Passedout_Year=forms.DateField(widget = forms.SelectDateWidget)
#     Resume=forms.FileField(max_length=10)
#     # class Meta:
    #     model=registration,
    #     fields=("first_name","last_name","username","email","mobile","Password","Hihest_Qualification","Passedout_Year","Resume")
   
    
#     def __str__(self):
#         return self.first_name
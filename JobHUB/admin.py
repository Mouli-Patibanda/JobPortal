from django.contrib import admin
from django import forms

# Register your models here.
from .models import registration,company_registration,jobcreate
class registrationAdminForm(forms.ModelForm):
    class Meta:
        model = registration
        fields = '__all__'
        widgets = {
            'Highest_Qualification': forms.RadioSelect,
        }
class registrationAdmin(admin.ModelAdmin):
  list_display=("first_name","last_name","username","email","password","mobile","Highest_Qualification","pdf_file")
class Company_registrationAdmin(admin.ModelAdmin):
   list_display=("username","email","password","mobile","company_name","role")
  
class jobcreateAdmin(admin.ModelAdmin):
  list_display=("company","experience","location","username","mobile","job_role")
   
            
admin.site.register(registration,registrationAdmin)
admin.site.register(company_registration,Company_registrationAdmin)
admin.site.register(jobcreate,jobcreateAdmin)
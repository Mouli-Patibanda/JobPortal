from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from django.http import HttpResponse
from django.template import loader
# from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import registration,company_registration,jobcreate
from django.contrib import admin
from django.core.files.storage import FileSystemStorage

@login_required(login_url="user_login")
def home(request):
    username = request.user.username
    user = registration.objects.get(username=username)
    return render(request, 'home.html', {'user': user})
def user_registration(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        mobile=request.POST['mobile']
        Highest_Qualification=request.POST.get('Highest_Qualification')
        file1 = registration()
        file1.Highest_Qualification = Highest_Qualification
        file1.save()
        pdf_file = request.FILES['pdf_file']
        document = registration(pdf_file=pdf_file)
        document.save()
        if password1==password2:
            if User.objects.filter(username=username):
                messages.info(request,'Username Taken') 
                return redirect('user_registration')
            elif User.objects.filter(email=email):
                messages.info(request,'Email Taken') 
                return redirect('user_registration') 
            else:
                user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,password=password1)
                user.save()
                user1=registration(first_name=first_name, last_name=last_name, username=username, email=email,password=password1,mobile=mobile,Highest_Qualification=Highest_Qualification,pdf_file=pdf_file)
                user1.save()
               
                return redirect('user_login')
        else:
             messages.info(request,'Password not matching') 
             return redirect('user_registration')
       
    else:
        return render(request,"user_registration.html") 

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            # return HttpResponse(password,username,user)
            messages.info(request,'Invalid Credentials')
            return redirect("user_login")
    else:
        return render(request, "user_login.html")


    
def logOut(request):
    logout(request)
    return redirect("user_login")
    
def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render())

def profile(request,id):
    myid = registration.objects.get(id=id)
    template=loader.get_template('profile.html')
    values={
        'myid':myid,
    }
    if request.method =='POST':
        return redirect("home")
    return HttpResponse(template.render(values,request))
 

def companyRegistration(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        mobile=request.POST['mobile']
        company_name=request.POST['company_name']
        role=request.POST['role']
        if password1==password2:
            if User.objects.filter(username=username):
                messages.info(request,'Username Taken') 
                return redirect('companyRegistration')
            elif User.objects.filter(email=email):
                messages.info(request,'Email Taken') 
                return redirect('companyRegistration') 
            else:
                user=User.objects.create_user(username=username, email=email,password=password1)
                user.save()
                user1=company_registration(username=username,email=email,password=password1,mobile=mobile,company_name=company_name,role=role)
                user1.save()
                return redirect('job_creation')
        else:
             messages.info(request,'Password not matching') 
             return redirect('companyRegistration')
    else:
        return render(request,"companyRegistration.html") 

def job_creation(request):
  if request.method =='POST':
        username = request.POST.get('username')
        password=request.POST.get('password')
        company=request.POST.get('company')
        experience=request.POST.get('experience')
        job_role=request.POST.get('job_role')
        location=request.POST.get('location')
        mobile=request.POST.get('mobile')
        user=authenticate(request, username = username, password = password)
        if (user is not None):
            useR=jobcreate(job_role=job_role,company=company,experience=experience,location=location,username=username,mobile=mobile)
            useR.save()
            login(request, user)
          
            return redirect('job_creation') 
        else:
            messages.info(request,'Invalid Credentials')
            return redirect("job_creation")
  else:
        return render(request, "job_creation.html")     
def java_developer(request):
    java=jobcreate.objects.filter(job_role='Java developer')
    context={
      'java':java,
       }
    template=loader.get_template('java_developer.html')
    return HttpResponse(template.render(context,request))
    
def python_developer(request):
    Python=jobcreate.objects.filter(job_role='Python developer')
    context={
      'Python':Python,
       }
    template=loader.get_template('python_developer.html')
    return HttpResponse(template.render(context,request))
def react_developer(request):
    React=jobcreate.objects.filter(job_role='React developer')
    context={
      'React':React,
       }
    template=loader.get_template('react_developer.html')
    return HttpResponse(template.render(context,request))
def angular_developer(request):
    Angular=jobcreate.objects.filter(job_role='Angular developer')
    context={
      'Angular':Angular,
       }
    template=loader.get_template('angular_developer.html')
    return HttpResponse(template.render(context,request))

def success(request):
    template=loader.get_template('success.html')
    return HttpResponse(template.render())
def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
    
    
      

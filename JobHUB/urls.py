from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns=[
    path('user_registration/', views.user_registration, name="user_registration"),
    path('user_login/', views.user_login, name="user_login"),
    path('', views.welcome, name="welcome"),
    path('home/', views.home, name="home"),
    path("logOut/",views.logOut, name="logOut"),
    path('Profile<int:id>)' ,views.profile, name="Profile"),
    path('companyRegistration/', views.companyRegistration, name="companyRegistration"),
    path('job_creation/',views.job_creation, name="job_creation"),
    path('java_developer/',views.java_developer,name="java_developer"),
    path('python_developer/',views.python_developer,name="python_developer"),
    path('react_developer/',views.react_developer,name="react_developer"),
    path('angular_developer/',views.angular_developer,name="angular_developer"),
    path('success/', views.success, name="success"),
    path('index/', views.index, name="index"),
    # path('create_job/',views.create_job, name="create_job"),
    # path('job/',views.job,name="job")
]
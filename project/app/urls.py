
from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='servies'),
    path("login",views.login,name="logn"),
    path("register",views.register,name="register"),
    path("forgot",views.forgot,name="forgot"),
    path("edu_login",views.edu_login,name='edu_login'),
    path("edu_register",views.edu_register,name="edu_register",)

]


from django.contrib import admin
from django.urls import path,include
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index,name='index'),
    path("index",views.index,name="index"),
    path("about",views.about,name='about'),
    path("services",views.services,name='servies'),
    path("login",views.do_login,name="login"),
    path("register",views.register,name="register"),
    path("forgot",views.forgot,name="forgot"),
    path("edu_login",views.edu_login,name='edu_login'),
    path("edu_register",views.edu_register,name="edu_register",),
    path("contact",views.contact,name='contact'),
    path('profile',views.profile,name="profile"),
    path('profile_update',views.profile_update,name="profile_update"),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('courses',views.courses,name='courses'),
    path('course/<int:course_id>/',views.course_detail,name='course_detail'),
    path('course/<int:course_id>/<int:video_id>/', views.video_detail, name='video_detail'),
]

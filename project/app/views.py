from django.shortcuts import render,HttpResponse,redirect,get_object_or_404 
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from app.Emailbackend import EmailBackEnd
from django.contrib.auth.decorators import login_required
from app.models import *
# Create your views here.
def index(request):
    course=Course.objects.all()
    print(course)
    context={'courses':course,}
    return render(request,"index.html",context)
def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def do_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=EmailBackEnd.authenticate(request,username=username,password=password)
        if user!=None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'Email and Password are Invalid')
            return redirect('login')


    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email already exists')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.warning(request,"User name already exists")
            return redirect('register')
    
    
        user=User(username=username, email=email,)
        user.set_password(password)
        user.save()
    return render(request,"register.html")
def forgot(request):
    return render(request,"forgot.html")

def edu_login(request):
    return render(request,"edu_login.html")

def edu_register(request):
    return render(request,"educator_register.html")

def contact(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject="Contact Form"
            message = f'Name: {form.cleaned_data["name"]}\nEmail: {form.cleaned_data["email"]}\nMessage: {form.cleaned_data["message"]}'
            from_email=form.cleaned_data['email']
            admin_email='projectdemocs699@zohomail.in'
            send_mail(subject,message,from_email,[admin_email])
            return redirect('index')
        else:
            form=ContactForm()
    return render(request,"contact.html")

@login_required(login_url='login')
def profile(request):
    return render(request,"profile.html")

@login_required(login_url='login')
def profile_update(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')

def courses(request):
    course=Course.objects.all()
    print(course)
    context={'courses':course,}
    return render(request,'Courses.html',context)
def course_detail(request,course_id):
    course=get_object_or_404(Course, pk=course_id)
    videos=course.videos.all()
    return render(request,'course_detail.html',{'course':course,'videos':videos})

def video_detail(request,course_id,video_id):
    course=get_object_or_404(Course,pk=course_id)
    video=get_object_or_404(Video,pk=video_id,course=course)
    return render(request,'video_detail.html',{'course': course, 'video': video})
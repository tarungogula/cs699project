from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def forgot(request):
    return render(request,"forgot.html")

def edu_login(request):
    return render(request,"edu_login.html")

def edu_register(request):
    return render(request,"educator_register.html")
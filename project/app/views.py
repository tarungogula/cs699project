from django.shortcuts import render,HttpResponse,redirect,get_object_or_404 
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from app.Emailbackend import EmailBackEnd
from django.contrib.auth.decorators import login_required
from app.models import *
from django.forms import inlineformset_factory
from .forms import *

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
            return redirect('courses')
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user!=None:
            login(request,user)
            return redirect('courses')
        else:
            messages.error(request,'Email and Password are Invalid')
            return redirect('edu_login')
    return render(request,"edu_login.html")

def edu_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username, email, password)

        author = Author.objects.create(name=user)

        return redirect('index') 

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
        return redirect('profile')

@login_required(login_url='login')
def courses(request):
    if request.method == 'POST':
        return add_course(request)
    is_author = False

    if request.user.is_authenticated:
        # Check if the user has an associated Author model
        try:
            author_profile = request.user.author
            is_author = True
        except Author.DoesNotExist:
            is_author = False

    course=Course.objects.all()
    context={'courses':course,'is_author':is_author}
    return render(request,'Courses.html',context)

def video_detail(request,course_id,video_id):
    course=get_object_or_404(Course,pk=course_id)
    video=get_object_or_404(Video,pk=video_id,course=course)
    return render(request,'video_detail.html',{'course': course, 'video': video})

def add_course(request):
    if not request.user.is_authenticated or not hasattr(request.user, 'author'):
        return redirect('edu_login') 
    AuthorCourseFormSet = inlineformset_factory(Author, Course, form=CourseForm, extra=1)
    VideoFormSet = inlineformset_factory(Course, Video, form=VideoForm, extra=1,can_delete=True)

    author = Author.objects.get(name=request.user)  

    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)
        video_formset = VideoFormSet(request.POST, prefix='videos')

        if course_form.is_valid() and video_formset.is_valid():
            # Save the course
            course = course_form.save(commit=False)
            course.author = author
            course = course_form.save()

            # Save the videos associated with the course
            videos = video_formset.save(commit=False)
            for video in videos:
                video.course = course
                video.save()


            return redirect('courses')
    else:
        print("redirected again to same page")
        course_form = CourseForm()
        video_formset = VideoFormSet(prefix='videos')

    context = {
        'course_form': course_form,
        'video_formset': video_formset,
    }

    return render(request, 'add_course.html', context)


def enroll_course(request, course_id):
    if request.user.is_authenticated and hasattr(request.user, 'student'):
        student = request.user.student
        course = get_object_or_404(Course, id=course_id)
        
        # Check if the student is already enrolled in the course
        if not Enrollment.objects.filter(student=student, course=course).exists():
            # Enroll the student in the course
            Enrollment.objects.create(student=student, course=course)
        else:
            messages.warning(request, 'You are already enrolled in this course.')

    return redirect('courses')  # Redirect to the courses page


def course_detail(request,course_id):
    course=get_object_or_404(Course, pk=course_id)
    videos=course.videos.all()
    return render(request,'course_detail.html',{'course':course,'videos':videos})


def modify_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    VideoFormSet = inlineformset_factory(Course, Video, form=VideoForm, extra=1, can_delete=True)

    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES, instance=course)
        video_formset = VideoFormSet(request.POST, request.FILES, instance=course, prefix='videos')

        if course_form.is_valid() and video_formset.is_valid():
            course_form.save()
            video_formset.save()
            return redirect('courses')

    else:
        course_form = CourseForm(instance=course)
        video_formset = VideoFormSet(instance=course, prefix='videos')

    context = {
        'course_form': course_form,
        'video_formset': video_formset,
        'course': course,
    }

    return render(request, 'modify_course.html', context)

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        complaint = request.POST.get('complaint')

        # Send email to admin
        subject = 'User Complaint'
        message = f'User with email {email} has the following complaint:\n\n{complaint}'
        from_email ='projectdemocs699@zohomail.in'
        to_email = '23m0747@iitb.ac.in'  # Replace with your admin's email address

        send_mail(subject, message, from_email, [to_email])

        # Redirect to a thank you page or the same contact page with a success message
        return HttpResponseRedirect('/thank-you/')  # Update the URL as needed

    return render(request, 'contact.html')

def about(request):
    return render(request,'about.html')

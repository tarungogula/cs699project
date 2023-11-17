from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ContactSubmission(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()


    class Meta:
        app_label='app'
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolled_courses = models.ManyToManyField('Course', related_name='enrolled_students', blank=True)
    def __str__(self):
        return self.user.username

class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name.username
    

class Course(models.Model):
    image=models.ImageField(upload_to="Media/images",null=True)
    title=models.CharField(max_length=500)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    slug=models.SlugField(default='',max_length=500,null=True,blank=True)

    def __str__(self):
        return self.title
    
class Video(models.Model):
    course=models.ForeignKey(Course,related_name='videos', on_delete=models.CASCADE)
    title=models.CharField( max_length=50)
    video_url=models.URLField( max_length=200)
    def __str__(self):
        return self.title
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    


from django.db import models

# Create your models here.
class ContactSubmission(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

    class Meta:
        app_label='app'
class Author(models.Model):
    author_profile=models.ImageField(upload_to="Media/author")
    name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
    

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
    


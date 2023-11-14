from django import forms
from .models import Course, Video
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactSubmission
        fields=['name','email','message']
class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['title','author','image']
class VideoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=['title','video_url']
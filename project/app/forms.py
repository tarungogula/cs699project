from django import forms
from .models import Course, Video
from .models import ContactSubmission
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory


class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactSubmission
        fields=['name','email','message']
class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['title','image']
    def clean_title(self):
        title = self.cleaned_data['title']
        existing_course = Course.objects.filter(title=title).exclude(pk=self.instance.pk)

        if existing_course.exists():
            raise ValidationError("A course with this title already exists.")

        return title
class VideoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=['id','title','video_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Video Title'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Video URL'}),
        }
VideoFormSet = inlineformset_factory(Course, Video, form=VideoForm, extra=5, can_delete=True)

from django import forms
from .models import Course, Video
from .models import ContactSubmission
from django.core.exceptions import ValidationError

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
        fields=['title','video_url']
VideoFormSet = forms.modelformset_factory(
    Video, form=VideoForm, extra=1, can_delete=True
)
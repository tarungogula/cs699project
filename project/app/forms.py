from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Mets:
        model=ContactSubmission
        fields=['name','email','message']
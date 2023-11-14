from django.contrib import admin
from .models import *

admin.site.register(ContactSubmission)
# Register your models here.

admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Video)
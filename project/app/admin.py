from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Video)

admin.site.register(Student)
admin.site.register(Enrollment)
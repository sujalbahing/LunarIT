from django.contrib import admin
from .models import *

admin.site.register(Course)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Image','Description','Price']
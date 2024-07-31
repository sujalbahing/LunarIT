from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(About)
admin.site.register(Product)
admin.site.register(Contact)

class AboutAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Title','Image','Description']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Image','Description','Price']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Email','Subject','Phone','Message']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Image','Description','Price']
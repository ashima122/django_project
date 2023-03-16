from django.contrib import admin
from .models import *


class UploadImageAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'image']
admin.site.register(UploadImage, UploadImageAdmin)
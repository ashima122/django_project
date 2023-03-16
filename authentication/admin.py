from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'email', 'phone_number', 'is_staff','is_active', "role", "is_superuser"]
admin.site.register(User, UserAdmin)
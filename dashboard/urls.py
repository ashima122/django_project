from django.urls import path, include
from .views import * 

urlpatterns = [
    path('', dashboard),
    path("logout",logout_user),
    path('upload', upload_images)
]
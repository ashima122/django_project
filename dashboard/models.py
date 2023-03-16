from django.db import models
from authentication.models import User

# Create your models here.

def get_upload_path(instance, filename):
    return f"{instance.user.role}/{instance.user.email}/{filename}"
class UploadImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to=get_upload_path)

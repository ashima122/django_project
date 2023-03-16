from django import forms
from .models import UploadImage

class ImageForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }

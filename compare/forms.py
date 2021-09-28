
from .models import ImageUploadModel
from django import forms

class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = ('document',)



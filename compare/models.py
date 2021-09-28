from django.db import models
from django.contrib.auth.models import User
class ImageUploadModel(models.Model):
    blog_id = models.IntegerField(default=0)
    sim=models.IntegerField(default=0)
    best_character=models.CharField(max_length=10,default="None")
    document = models.ImageField(upload_to = 'images/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.blog_id

class Charac(models.Model):
    name=models.CharField(max_length=10)
    imgurl=models.CharField(max_length=300)
    def __str__(self):
        return self.name


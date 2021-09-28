from django.shortcuts import render
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from django.conf import settings
from .opencv_dface import main
from .models import ImageUploadModel

def dface(request,username):
    if request.method =='POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            imageURL = settings.MEDIA_URL + form.instance.document.name
            (sim,best,user_image)=main(settings.MEDIA_ROOT_URL + imageURL)
            post.sim=sim
            post.best_character=best
            post.save()
            return render(request,'dface.html',{'form':form,'post':post,'sim':sim,'best':best,
            'username':username,'user_image':user_image})
    else:
        form = ImageUploadForm()
    return render(request, 'dface.html',{'form':form,'username':username,})









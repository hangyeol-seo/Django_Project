from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Blog
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import connection
from django.db.models import Max,Min
from django.apps import apps
from compare.models import ImageUploadModel

def home(request,username):
    blogs=Blog.objects
    return render(request, 'home.html', {'blogs': blogs,'username':username})

def first(request):
    return render(request,'first.html')
    
def detail(request, blog_id, username):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    
    MyModel=apps.get_model('compare','ImageUploadModel')
    value=MyModel.objects.filter(blog_id=-1)
    if(value):
        obj=MyModel.objects.get(blog_id=-1)
        obj.blog_id=blog_id
        obj.save()
    target=MyModel.objects.get(blog_id=blog_id)
    user_image=target.document
    sim=target.sim
    best=target.best_character

    ScoreModel=apps.get_model('polls','Choice')
    choice1=ScoreModel.objects.get(id =2)
    choice2=ScoreModel.objects.get(id=4)
    choice3=ScoreModel.objects.get(id=6)
    choice4=ScoreModel.objects.get(id=8)
    choice5=ScoreModel.objects.get(id=10)
    choices=[choice1,choice2,choice3,choice4,choice5]
    
    count=0
    
    for choice in choices:
        count+=choice.votes
    
    choices=ScoreModel.objects.all()
    for choice in choices:
        choice.votes=0
        choice.save()

    #BlogModel=apps.get_model('blog','Blog')
    #sql1="update blog_blog set writer=%s where id=%s"
    #sql2="update blog_blog set score=%s where id=%s"
    #with connection.cursor() as cursor:
    #    cursor.execute(sql1,[username,blog_id])
    #with connection.cursor() as cusor:
    #    cursor.execute(sql2,[count,blog_id])

    man=Blog.objects.get(id=blog_id)
    if(man.writer=="admin"):
        man.writer=username
        man.score=count
        man.save()

    writer=man.writer
    score=man.score

    return render(request, 'detail.html',{'blog':blog_detail,
    'username':username,'user_image':user_image,'writer':writer,'score':score,
    'sim':sim,'best':best})

def new(request,username):
    MyModel=apps.get_model('compare','ImageUploadModel')
    obj=MyModel.objects.aggregate(id=Max('id'))
    image_id=obj['id']
    value=MyModel.objects.get(pk=image_id)
    value.blog_id=-1
    value.save()
    return render(request, 'new.html',{'username':username})
def create(request,username):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    blog_id=blog.id
    return HttpResponseRedirect(reverse('detail',args=(blog_id,username)))
    #return redirect('/blog/'+str(blog.id))
# Create your views here.

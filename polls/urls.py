from django.contrib import admin
from django.urls import path
from . import views

app_name='polls'
urlpatterns=[
    path('<str:username>',views.index, name='index'),
    path('<int:question_id>/<str:username>',views.question_detail, name='question_detail'),
    path('<int:question_id>/<str:username>/vote/',views.vote,name='vote'),
]
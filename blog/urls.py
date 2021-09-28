from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('<int:blog_id>/<str:username>',views.detail, name='detail'),
    path('<str:username>/new', views.new, name='new'),
    path('<str:username>/create',views.create, name='create'),
]
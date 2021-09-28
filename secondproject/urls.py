from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import blog.views
import accounts.views
import polls.views
import compare.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.first,name='first'),
    path('<str:username>/home',blog.views.home, name='home'),
    path('blog/',include('blog.urls')),
    path('accounts/',include('accounts.urls')),
    path('polls/',include('polls.urls')),
    path('compare/',include('compare.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

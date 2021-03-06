"""facebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from myapp import views
from django.conf.urls.static import static
from django.conf import settings
from myapp.views import index, add
from myapp.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index, name="index"),
    url(r'^clickpic/(?P<pk>\d+)/$',views.add,name="add"),
    url(r'^comment/(?P<pk>\d+)/$',views.comment,name="comment"),    
    url(r'^upload', views.uploadImg, name="upload"),
    url(r'^space/(?P<pk>\w+)/$', views.space, name="space"),
    url(r'^profile', views.profile, name="profile"),
    url(r'^$', 'django.contrib.auth.views.login'),
   
   
    # url(r'^home/$', home, name = "home"),
    url(r'^register/$', register),
    # url(r'^register/success/$', register_success),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# {% url "add" post.pk %} 
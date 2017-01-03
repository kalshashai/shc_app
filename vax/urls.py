"""shc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'home'),
    url(r'^about/$', views.about, name = 'about'),
    #Child's
    url(r'^child/$', views.ChildList.as_view() , name = 'child_list'),
    url(r'^child/(?P<pk>\d+)/$', views.ChildDetail.as_view(), name = 'child_show'),
    url(r'^child/add$', views.ChildCreate.as_view(), name = 'child_add'),
    url(r'^child/(?P<pk>\d+)/edit/$', views.ChildUpdate.as_view(), name = 'child_update'),
    url(r'^child/(?P<pk>\d+)/delete$', views.ChildDelete.as_view(), name = 'child_delete'),
    #Mother
    url(r'^mother/$', views.MotherList.as_view() , name = 'mother_list'),
    url(r'^mother/(?P<pk>\d+)/$', views.MotherDetail.as_view(), name = 'mother_show'),
    url(r'^mother/add$', views.MotherCreate.as_view(), name = 'mother_add'),
    url(r'^mother/(?P<pk>\d+)/edit/$', views.MotherUpdate.as_view(), name = 'mother_update'),
    url(r'^mother/(?P<pk>\d+)/delete$', views.MotherDelete.as_view(), name = 'mother_delete'),
]

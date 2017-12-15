from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from research.models import Post
from . import views


urlpatterns = [
    url(r'^$', views.base, name='base')]

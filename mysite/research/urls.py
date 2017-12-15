from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from research.models import Bioscience
from . import views

urlpatterns = [
    url(r'^$', views.indexH, name='indexH')]

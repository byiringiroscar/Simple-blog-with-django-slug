from django.urls import path

from . import views

name = 'registerr'

urlpatterns = [
    path('', views.home, name='home'),


]


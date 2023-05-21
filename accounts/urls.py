from django.urls import path

from . import views

name = 'accounts'

urlpatterns = [
    path('register', views.register, name='register')
]
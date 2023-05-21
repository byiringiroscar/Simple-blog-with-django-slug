from django.urls import path
from .import views

name = 'bic'

urlpatterns = [
    path('', views.bic, name='bic')

]
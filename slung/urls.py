from django.urls import path
from .import views
name = 'slung'

urlpatterns = [
    # path('', views.slung, name='slung'),
    path("<single_slug>", views.single_slug, name="single_slug"),
    path("", views.slug, name="slug"),
    path("bean", views.bean, name="bean")
]

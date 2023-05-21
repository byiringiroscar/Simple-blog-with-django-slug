from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.


def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        return HttpResponse(f"{single_slug} is a category!!!")
    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in categories:
        return HttpResponse(f"{single_slug} is a category!!!")
    return HttpResponse(f"{single_slug} does not corresponding to anything")


# def slung(request):
#     return render(request, 'categories.html', context={'categories': TutorialCategory.objects.all()})


def slug(request):
    team = Team.objects.all()
    context = {
        'team': team
    }
    return render(request, 'team.html', context)


def bean(request):
    bean = Player.objects.all()
    context = {
        'bean':bean
    }
    return render(request, 'players.html', context)

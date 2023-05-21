from django.shortcuts import render
from .models import Car_registration,Tax,Control,Insurance

# Create your views here.

plate_number = 'RAD520G'


def bic(request):
    plate_unique = Car_registration.objects.get(plate_number=plate_number)

    context = {
        'plate': plate_number
    }
    return render(request, 'html/bic.html')

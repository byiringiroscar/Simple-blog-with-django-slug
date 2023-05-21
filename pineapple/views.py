from django.shortcuts import render
from .models import Control, Car_registration, Tax, Insurance

# Create your views here.

plate_number = 'RAA123F'


def check(requests):
    return render(requests, 'html/index.html')


def capture_plate(requests):
    phone_n = Car_registration.objects.filter(plate_number=plate_number)
    plate_n = Car_registration.objects.filter(plate_number=plate_number)
    tax_n = Tax.objects.all()
    insu_n = Insurance.objects.all()
    control_n = Control.objects.all()

    for phone in phone_n:
        phoneN = phone.phonenumber

    context = {
        'insurance': Insurance.objects.all(),
        'tax': Tax.objects.all(),
        'control': Control.objects.all(),
        'cars': Car_registration.objects.all(),
        'search': Car_registration.objects.all().get(plate_number=plate_number),
        'plate_number': plate_number,
        'phone_n': phone_n,
        'tax_n': tax_n,
        'insu_n': insu_n,
        'control_n ': control_n,
        'phoneN': phoneN,


    }



    return render(requests, 'html/dashboard.html', context)

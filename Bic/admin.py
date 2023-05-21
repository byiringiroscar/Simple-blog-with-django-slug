from django.contrib import admin
from Bic.models import Car_registration, Control, Insurance, Tax
# Register your models here.

admin.site.register(Car_registration)
admin.site.register(Control)
admin.site.register(Insurance)
admin.site.register(Tax)


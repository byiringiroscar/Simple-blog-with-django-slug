from django.db import models


# Create your models here.


class Car_registration(models.Model):
    plate_number = models.CharField(primary_key=True, max_length=200, null=False)
    car_owner = models.CharField(max_length=200, null=False)
    Owner_Id = models.IntegerField()
    phonenumber = models.CharField(max_length=50, default=0)
    car_model = models.CharField(max_length=200, null=False)
    color = models.CharField(max_length=100, null=False)
    Time_done = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.plate_number}'

    class Meta:
        verbose_name_plural = "Car_registration"


class Control(models.Model):
    car_registration = models.ManyToManyField(Car_registration, related_query_name='car_re')

    control_status = models.BooleanField(default=False)
    time_done = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.self.car_registration}'

    class Meta:
        verbose_name_plural = "Control"


class Tax(models.Model):
    car_registration = models.ManyToManyField(Car_registration)

    tax_status = models.BooleanField(default=False)
    time_done = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.self.car_registration}'

    class Meta:
        verbose_name_plural = "Tax"


class Insurance(models.Model):
    car_registration = models.ManyToManyField(Car_registration)
    it_plate = models.CharField(max_length=50, null=True)
    insurance_status = models.BooleanField(default=False)  # if this check status is True means that car paid insurance
    time_done = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.self.car_registration}'

    class Meta:
        verbose_name_plural = "Insurance"

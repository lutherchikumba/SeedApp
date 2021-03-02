
from django.db import models
from django.utils import timezone


class Grower(models.Model):
    grower_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=True)
    email = models.EmailField(unique=True, blank=False, null=True)
    phone = models.CharField(max_length=10, blank=False, null=True)
    zip_code = models.IntegerField(blank=False, null=True)


class Trial(models.Model):
    trial_id = models.BigAutoField(primary_key=True)
    grower_id = models.ForeignKey(Grower, on_delete=models.CASCADE,  null=True)
    latitude = models.FloatField(blank=False, null=True)
    longitude = models.FloatField(blank=False, null=True)
    crop = models.CharField(max_length=50, blank=False, null=True)
    date = models.DateField(default=timezone.now, blank=False, null=True)
    notes = models.CharField(max_length=50, blank=False, null=True)
    user = models.CharField(max_length=50, null=True)


class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    trial_id = models.ForeignKey(Trial, on_delete=models.CASCADE, blank=True, null=True)
    product = models.CharField(max_length=50, blank=False, null=True)
    timing = models.CharField(max_length=50, blank=False, null=True)
    rate = models.FloatField(blank=False, null=True)
    rate_unit = models.CharField(max_length=50, blank=False, null=True)
    treatment_id = models.CharField(max_length=50, blank=False, null=True)
    


class Measure(models.Model):
    measure_id = models.BigAutoField(primary_key=True)
    trial_id = models.ForeignKey(Trial, on_delete=models.CASCADE, blank=True, null=True)
    measure = models.CharField(max_length=50, blank=False, null=True)
    unit = models.CharField(max_length=50, blank=False, null=True)
    timing = models.CharField(max_length=50, blank=False, null=True)
    value = models.FloatField(blank=False, null=True)
    type = models.CharField(max_length=50, blank=False, null=True)

class Treatment(models.Model):
    treatment_id = models.BigAutoField(primary_key=True)
    trial_id = models.ForeignKey(Trial, on_delete=models.CASCADE, blank=True, null=True)
    treatment = models.CharField(max_length=50, blank=False, null=True)
    unit = models.CharField(max_length=50, blank=False, null=True)
    timing = models.CharField(max_length=50, blank=False, null=True)
    value = models.FloatField(blank=False, null=True)
    type_of_treatment = models.CharField(max_length=50, blank=False, null=True)
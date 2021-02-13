from django.db import models
from django.utils import timezone


class Grower(models.Model):
    grower_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=True)
    email = models.EmailField(unique=True, blank=False, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    zip = models.IntegerField(blank=False, null=True)
    user = models.CharField(max_length=100, null=True)


class Trial(models.Model):
    trial_id = models.BigAutoField(primary_key=True)
    grower_id = models.ForeignKey(Grower, on_delete=models.CASCADE,  null=True)
    latitude = models.FloatField(blank=False, null=True)
    longitude = models.FloatField(blank=False, null=True)
    crop = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    user = models.CharField(max_length=100, null=True)


class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    trial_id = models.ForeignKey(Trial, on_delete=models.CASCADE, blank=True, null=True)
    product = models.CharField(max_length=150, blank=True, null=True)
    timing = models.CharField(max_length=150, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    rate_unit = models.CharField(max_length=150, blank=True, null=True)
    treatment_id = models.CharField(max_length=50, blank=True, null=True)


class Measure(models.Model):
    measure_id = models.BigAutoField(primary_key=True)
    trial_id = models.ForeignKey(Trial, on_delete=models.CASCADE, blank=True, null=True)
    measure = models.CharField(max_length=150, blank=True, null=True)
    unit = models.CharField(max_length=150, blank=True, null=True)
    timing = models.CharField(max_length=150, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    treatment_id = models.CharField(max_length=50, blank=True, null=True)
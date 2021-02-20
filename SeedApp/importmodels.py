# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TrialsGrower(models.Model):
    grower_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trials_grower'


class TrialsMeasure(models.Model):
    measure_id = models.BigAutoField(primary_key=True)
    measure = models.CharField(max_length=150, blank=True, null=True)
    unit = models.CharField(max_length=150, blank=True, null=True)
    timing = models.CharField(max_length=150, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    trial_id = models.ForeignKey('TrialsTrial', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trials_measure'


class TrialsProduct(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product = models.CharField(max_length=150, blank=True, null=True)
    timing = models.CharField(max_length=150, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    rate_unit = models.CharField(max_length=150, blank=True, null=True)
    treatment_id = models.CharField(max_length=50, blank=True, null=True)
    trial_id = models.ForeignKey('TrialsTrial', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trials_product'


class TrialsTrial(models.Model):
    trial_id = models.BigAutoField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    crop = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    grower_id = models.ForeignKey(TrialsGrower, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trials_trial'

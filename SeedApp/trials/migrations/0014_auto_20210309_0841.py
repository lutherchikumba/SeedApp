# Generated by Django 3.1.6 on 2021-03-09 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0013_auto_20210307_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='hybrid',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rate_unit',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='timing',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

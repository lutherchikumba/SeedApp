# Generated by Django 3.1.6 on 2021-04-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0012_merge_20210407_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropList',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
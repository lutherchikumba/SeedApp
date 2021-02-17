# Generated by Django 3.1.6 on 2021-02-17 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0002_product_treatment_trial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groer',
            fields=[
                ('grower_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('zip', models.IntegerField(null=True)),
                ('user', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='trial',
            name='grower_id',
        ),
        migrations.DeleteModel(
            name='Grower',
        ),
    ]

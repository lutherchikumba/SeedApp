# Generated by Django 3.1.6 on 2021-02-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0009_remove_grower_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grower',
            old_name='zip',
            new_name='zip_code',
        ),
        migrations.AlterField(
            model_name='grower',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

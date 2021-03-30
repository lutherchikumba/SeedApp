# Generated by Django 3.1.6 on 2021-03-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0006_treatment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='rate_unit',
            new_name='unit',
        ),
        migrations.RenameField(
            model_name='treatment',
            old_name='timing',
            new_name='treatment_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='treatment_id',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='unit',
        ),
        migrations.AddField(
            model_name='product',
            name='treatment',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
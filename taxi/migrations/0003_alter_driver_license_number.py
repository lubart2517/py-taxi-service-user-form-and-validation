# Generated by Django 4.1 on 2023-09-23 15:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_alter_driver_license_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='license_number',
            field=models.CharField(error_messages={'regex': 'Must Consist only of 8 characters First 3 characters are uppercase lettersLast 5 characters are digits', 'unique': 'You entered existing number'}, max_length=255, unique=True, validators=[django.core.validators.RegexValidator('\\A[A-Z]{3}[0-9]{5}\\Z')]),
        ),
    ]

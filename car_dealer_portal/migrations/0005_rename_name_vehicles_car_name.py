# Generated by Django 4.0.3 on 2024-04-17 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealer_portal', '0004_rename_car_name_vehicles_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicles',
            old_name='name',
            new_name='car_name',
        ),
    ]

# Generated by Django 3.2.13 on 2022-04-25 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0002_client_staff'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=255)),
                ('assigned', models.BooleanField(default=False)),
                ('vehicle_type', models.CharField(blank=True, choices=[('TRUCK', 'Truck'), ('SUV', 'Suv'), ('SEDAN', 'Sedan'), ('JEEP', 'Jeep')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AllocatedVehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('towing_in_date', models.DateTimeField()),
                ('towing_out_date', models.DateTimeField()),
                ('towing_out', models.BooleanField(default=False)),
                ('payment_id', models.CharField(max_length=200)),
                ('allocated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('client_assigned', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.client')),
                ('vehicle_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allocated_vehicle', to='tow.vehicles')),
            ],
        ),
    ]

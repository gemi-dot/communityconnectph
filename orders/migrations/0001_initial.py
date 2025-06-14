# Generated by Django 4.2.22 on 2025-06-08 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaterStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WaterRefillRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('container_type', models.CharField(choices=[('5 Gallon', '5 Gallon'), ('3 Gallon', '3 Gallon'), ('Others', 'Others')], max_length=20)),
                ('quantity', models.PositiveIntegerField()),
                ('preferred_delivery_time', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Assigned', 'Assigned'), ('Completed', 'Completed')], default='Pending', max_length=20)),
                ('assigned_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.waterstation')),
            ],
        ),
    ]

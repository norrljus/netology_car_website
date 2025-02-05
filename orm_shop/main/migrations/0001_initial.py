# Generated by Django 5.1.3 on 2024-12-06 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('color', models.CharField(max_length=10)),
                ('mileage', models.IntegerField()),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('body_type', models.CharField(max_length=15)),
                ('drive_unit', models.CharField(max_length=10)),
                ('gearbox', models.CharField(max_length=10)),
                ('fuel_type', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.car')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
    ]

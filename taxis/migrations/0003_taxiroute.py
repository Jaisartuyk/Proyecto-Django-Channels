# Generated by Django 5.1.4 on 2024-12-26 03:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxis", "0002_appuser_national_id_appuser_phone_number_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaxiRoute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_available", models.BooleanField(default=False)),
                (
                    "passenger_1",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "passenger_2",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "passenger_3",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "passenger_4",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("estimated_arrival_time", models.DateTimeField(blank=True, null=True)),
                (
                    "taxi",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="taxis.taxi"
                    ),
                ),
            ],
        ),
    ]

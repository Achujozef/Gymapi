# Generated by Django 4.2.7 on 2024-03-06 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_rename_place_gymowner_city_gymowner_district_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserWeight",
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
                ("weight", models.FloatField()),
                ("measured_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="weights",
                        to="api.gymuser",
                    ),
                ),
            ],
        ),
    ]

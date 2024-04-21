# Generated by Django 4.2.7 on 2024-04-21 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0013_dietplan_dietplanday_dietplantiming"),
    ]

    operations = [
        migrations.CreateModel(
            name="DietAssignment",
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
                ("assigned_date", models.DateField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "diet_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.dietplan"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.gymuser"
                    ),
                ),
            ],
        ),
    ]

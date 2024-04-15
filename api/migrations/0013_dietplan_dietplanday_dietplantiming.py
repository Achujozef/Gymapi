# Generated by Django 4.2.7 on 2024-04-09 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0012_gymplan_image_gymplan_terms_and_conditions_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DietPlan",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "branch",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.branch",
                    ),
                ),
                (
                    "gym",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.gym"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DietPlanDay",
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
                ("day", models.CharField(max_length=20)),
                (
                    "diet_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="days",
                        to="api.dietplan",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DietPlanTiming",
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
                ("time", models.TimeField()),
                ("item_name", models.CharField(max_length=100)),
                ("is_done", models.BooleanField(default=False)),
                ("description", models.TextField(blank=True)),
                (
                    "diet_plan_day",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="timings",
                        to="api.dietplanday",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 5.0.1 on 2024-03-05 07:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GymEquipment",
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
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("cardio", "Cardio"),
                            ("strength", "Strength"),
                            ("free_weights", "Free Weights"),
                            ("machines", "Machines"),
                            ("other", "Other"),
                        ],
                        max_length=50,
                    ),
                ),
                ("manufacturer", models.CharField(max_length=100)),
                ("model_number", models.CharField(max_length=50)),
                ("purchase_date", models.DateField()),
                (
                    "purchase_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("warranty_information", models.TextField(blank=True, null=True)),
                ("warranty_expiration_date", models.DateField(blank=True, null=True)),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("used", "Used"),
                            ("refurbished", "Refurbished"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "maintenance_charge",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("availability", models.BooleanField(default=True)),
                ("image", models.CharField(blank=True, max_length=200, null=True)),
                ("additional_notes", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="OTP",
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
                ("phone", models.CharField(max_length=15)),
                ("otp", models.CharField(max_length=6)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Gym",
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
                ("name", models.CharField(default="Gym Name", max_length=100)),
                ("address", models.CharField(default="Address", max_length=100)),
                ("phone_number", models.CharField(default="1234567890", max_length=15)),
                ("email", models.EmailField(default="gym@example.com", max_length=254)),
                ("has_branches", models.BooleanField(default=False)),
                (
                    "owner",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Branch",
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
                ("name", models.CharField(default="Branch Name", max_length=100)),
                ("address", models.CharField(default="Branch Address", max_length=100)),
                (
                    "phone_number",
                    models.CharField(default="Branch Phone Number", max_length=15),
                ),
                (
                    "email",
                    models.EmailField(default="branch@example.com", max_length=254),
                ),
                (
                    "gym",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="branches",
                        to="api.gym",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attendance",
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
                ("date", models.DateField(auto_now_add=True)),
                ("time", models.TimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
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
            name="GymOwner",
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
                ("phone_number", models.CharField(max_length=15)),
                ("address", models.CharField(max_length=100)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GymPlan",
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
                ("name", models.CharField(default="Standard Plan", max_length=100)),
                ("description", models.TextField(default="Basic gym membership plan")),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
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
            name="Enquiry",
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
                ("name", models.CharField(default="Anonymous", max_length=100)),
                ("phone_number", models.CharField(default="", max_length=15)),
                ("place", models.CharField(default="", max_length=100)),
                ("email", models.EmailField(default="", max_length=254)),
                ("expected_joining_date", models.DateField(default="1900-01-01")),
                ("follow_up_date", models.DateField(default="1900-01-01")),
                ("enquiry_source", models.CharField(default="", max_length=100)),
                ("remarks", models.TextField(default="")),
                (
                    "added_by",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "branch",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.branch",
                    ),
                ),
                (
                    "gym",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.gym"
                    ),
                ),
                (
                    "plan",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.gymplan",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GymTrainer",
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
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other"),
                        ],
                        max_length=10,
                    ),
                ),
                ("date_of_birth", models.DateField()),
                ("contact_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("trainer_id", models.CharField(max_length=100)),
                ("certification_level", models.CharField(max_length=100)),
                ("certification_expiry_date", models.DateField()),
                ("education_and_training_background", models.TextField()),
                ("regular_working_hours", models.CharField(max_length=100)),
                ("areas_of_expertise", models.TextField()),
                ("specialized_certifications_or_skills", models.TextField()),
                ("bio", models.TextField()),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="trainer_profile_pictures/"
                    ),
                ),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "bonus_or_commission_information",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "documents",
                    models.FileField(
                        blank=True, null=True, upload_to="trainer_documents/"
                    ),
                ),
                ("emergency_contact_information", models.CharField(max_length=100)),
                ("health_conditions", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GymUser",
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
                ("gender", models.CharField(default="", max_length=10)),
                ("date_of_birth", models.DateField(default="1900-01-01")),
                ("contact_number", models.CharField(default="", max_length=15)),
                ("email", models.EmailField(default="", max_length=254)),
                ("address", models.TextField(default="")),
                ("joining_date", models.DateField(default="1900-01-01")),
                ("membership_expiry_date", models.DateField(default="1900-01-01")),
                (
                    "membership_status",
                    models.CharField(
                        choices=[
                            ("Active", "Active"),
                            ("Inactive", "Inactive"),
                            ("Suspended", "Suspended"),
                        ],
                        default="",
                        max_length=20,
                    ),
                ),
                ("membership_plan", models.CharField(default="", max_length=100)),
                ("health_conditions", models.TextField(default="")),
                ("fitness_goals", models.TextField(default="")),
                ("workout_schedule", models.TextField(default="")),
                ("exercise_restrictions", models.TextField(default="")),
                (
                    "emergency_contact_name",
                    models.CharField(default="", max_length=100),
                ),
                (
                    "emergency_contact_phone_number",
                    models.CharField(default="", max_length=15),
                ),
                (
                    "emergency_contact_relationship",
                    models.CharField(default="", max_length=100),
                ),
                ("membership_id_number", models.CharField(default="", max_length=50)),
                (
                    "access_information",
                    models.CharField(default="RFID", max_length=100),
                ),
                (
                    "assigned_personal_trainer",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "trainer_contact_information",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "assigned_locker_number",
                    models.CharField(blank=True, default="", max_length=20, null=True),
                ),
                ("feedback", models.TextField(blank=True, default="", null=True)),
                (
                    "documents",
                    models.FileField(blank=True, null=True, upload_to="documents/"),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="user_profile_pictures/"
                    ),
                ),
                ("weight", models.FloatField(blank=True, null=True)),
                (
                    "membership_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.gymplan",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Member",
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
                ("is_owner", models.BooleanField(default=False)),
                ("is_trainer", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_user", models.BooleanField(default=False)),
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
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("role", models.CharField(default="", max_length=100)),
                (
                    "salary",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("hire_date", models.DateField(default="1900-01-01")),
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
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

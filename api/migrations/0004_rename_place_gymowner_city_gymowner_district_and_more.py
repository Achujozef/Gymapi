# Generated by Django 4.2.7 on 2024-03-06 04:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_attendance_branch_gymequipment_branch_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="gymowner",
            old_name="place",
            new_name="city",
        ),
        migrations.AddField(
            model_name="gymowner",
            name="district",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="gymowner",
            name="state",
            field=models.CharField(default="", max_length=100),
        ),
    ]

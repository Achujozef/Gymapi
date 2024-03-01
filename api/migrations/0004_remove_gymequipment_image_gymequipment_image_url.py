# Generated by Django 5.0.1 on 2024-03-01 06:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_gymequipment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gymequipment",
            name="image",
        ),
        migrations.AddField(
            model_name="gymequipment",
            name="image_url",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

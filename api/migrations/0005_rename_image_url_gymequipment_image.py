# Generated by Django 5.0.1 on 2024-03-01 07:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_remove_gymequipment_image_gymequipment_image_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="gymequipment",
            old_name="image_url",
            new_name="image",
        ),
    ]
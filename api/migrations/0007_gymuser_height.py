# Generated by Django 4.2.7 on 2024-03-07 12:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0006_alter_gymequipment_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="gymuser",
            name="height",
            field=models.FloatField(blank=True, null=True),
        ),
    ]

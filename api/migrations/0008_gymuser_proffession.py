# Generated by Django 4.2.7 on 2024-03-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_gymuser_height"),
    ]

    operations = [
        migrations.AddField(
            model_name="gymuser",
            name="proffession",
            field=models.CharField(default="", max_length=100),
        ),
    ]

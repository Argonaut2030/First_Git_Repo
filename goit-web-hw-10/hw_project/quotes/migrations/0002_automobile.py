# Generated by Django 5.1.2 on 2024-11-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Automobile",
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
                ("producer", models.CharField(max_length=50)),
                ("type", models.CharField(max_length=50)),
                ("model_name", models.CharField(max_length=50)),
            ],
        ),
    ]

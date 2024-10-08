# Generated by Django 5.0.7 on 2024-07-16 17:23

import newsletter.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewsLetterEntry",
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
                    "entry_id",
                    models.CharField(
                        default=newsletter.utils.generate_entry_id,
                        max_length=255,
                        unique=True,
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("verified", models.BooleanField(default=False)),
            ],
        ),
    ]

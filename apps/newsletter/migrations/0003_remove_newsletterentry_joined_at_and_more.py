# Generated by Django 5.0.6 on 2024-07-09 13:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0002_rename_newsletter_newsletterentry"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newsletterentry",
            name="joined_at",
        ),
        migrations.AddField(
            model_name="newsletterentry",
            name="entry_id",
            field=models.CharField(default=uuid.uuid4, max_length=50),
        ),
        migrations.AddField(
            model_name="newsletterentry",
            name="verified",
            field=models.BooleanField(default=False),
        ),
    ]
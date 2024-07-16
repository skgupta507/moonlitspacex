# Generated by Django 5.0.7 on 2024-07-16 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
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
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField()),
                ("content", models.TextField()),
                (
                    "rendered_content",
                    models.TextField(blank=True, editable=False, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("readtime", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PinnedPost",
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
                ("cover", models.URLField()),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.blogpost"
                    ),
                ),
            ],
        ),
    ]
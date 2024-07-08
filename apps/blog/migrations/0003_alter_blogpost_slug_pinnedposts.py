# Generated by Django 5.0.6 on 2024-07-08 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_blogpost_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="slug",
            field=models.SlugField(),
        ),
        migrations.CreateModel(
            name="PinnedPosts",
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

# Generated by Django 3.1.7 on 2022-12-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Speaker",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField()),
                ("photo", models.URLField()),
                ("website", models.URLField()),
                ("description", models.TextField()),
            ],
        ),
    ]

# Generated by Django 3.1.7 on 2023-02-24 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_auto_20230224_1824"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "talk_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.talk",
                    ),
                ),
                ("slots", models.IntegerField()),
            ],
            options={
                "verbose_name": "Curso",
                "verbose_name_plural": "Cursos",
            },
            bases=("core.talk",),
        ),
    ]

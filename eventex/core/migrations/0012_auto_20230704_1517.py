# Generated by Django 3.1.7 on 2023-07-04 15:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_delete_courseold"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="talk",
            options={
                "ordering": ["start"],
                "verbose_name": "Palestra",
                "verbose_name_plural": "Palestras",
            },
        ),
    ]

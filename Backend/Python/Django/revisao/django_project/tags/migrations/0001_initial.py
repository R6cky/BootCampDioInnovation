# Generated by Django 4.2.4 on 2023-08-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("albums", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=255)),
                (
                    "albums",
                    models.ManyToManyField(related_name="tags", to="albums.album"),
                ),
            ],
        ),
    ]
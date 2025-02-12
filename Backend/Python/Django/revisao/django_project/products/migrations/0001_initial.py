# Generated by Django 4.2.4 on 2023-08-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=20)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Drink", "Drink"),
                            ("Meat", "Meat"),
                            ("Candy", "Candy"),
                            ("Fruit", "Fruit"),
                            ("Other", "Other"),
                        ],
                        default="Other",
                        max_length=30,
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
            ],
        ),
    ]

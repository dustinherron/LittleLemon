# Generated by Django 4.1.4 on 2023-08-09 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("Title", models.CharField(max_length=255)),
                ("Price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("Inventory", models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name="BookingTable",
            new_name="Booking",
        ),
    ]
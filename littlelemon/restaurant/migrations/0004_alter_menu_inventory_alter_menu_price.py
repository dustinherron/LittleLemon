# Generated by Django 4.1.4 on 2023-08-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0003_rename_inventory_menu_inventory_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="inventory",
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="menu",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]

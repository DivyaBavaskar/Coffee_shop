# Generated by Django 5.0.1 on 2024-02-07 10:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("coffeeapp", "0007_remove_customeraddress_customer_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartitem",
            old_name="pet",
            new_name="coffee",
        ),
    ]
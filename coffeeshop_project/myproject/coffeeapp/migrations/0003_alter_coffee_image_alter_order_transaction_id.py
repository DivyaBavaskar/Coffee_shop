# Generated by Django 5.0.1 on 2024-01-16 08:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coffeeapp", "0002_customer_order_customeraddress_orderitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coffee",
            name="image",
            field=models.ImageField(upload_to="coffee_images/"),
        ),
        migrations.AlterField(
            model_name="order",
            name="transaction_id",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]

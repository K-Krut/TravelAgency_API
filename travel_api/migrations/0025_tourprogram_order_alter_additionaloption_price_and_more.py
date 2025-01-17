# Generated by Django 4.2.3 on 2023-10-28 13:38

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travel_api", "0024_tourprogram_order_alter_order_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="additionaloption",
            name="price",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Ціна",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="is_primary_contact",
            field=models.BooleanField(
                default=False, verbose_name="Контакт для звʼязку"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="phone",
            field=models.CharField(null=True, verbose_name="Номер телефону"),
        )
    ]

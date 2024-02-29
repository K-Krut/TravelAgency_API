# Generated by Django 4.2.3 on 2023-12-20 14:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travel_api", "0036_tourprogram_order_alter_additionaloption_icon_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tourprogram",
            name="order",
            field=models.IntegerField(
                default=1,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Порядок",
            ),
        ),
    ]
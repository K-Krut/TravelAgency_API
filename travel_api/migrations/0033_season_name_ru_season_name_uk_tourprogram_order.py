# Generated by Django 4.2.3 on 2023-11-02 15:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travel_api", "0032_tourprogram_order_alter_tourdayoption_date_end_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="season",
            name="name_ru",
            field=models.CharField(
                max_length=255,
                null=True,
                validators=[django.core.validators.MinLengthValidator(3)],
                verbose_name="Назва",
            ),
        ),
        migrations.AddField(
            model_name="season",
            name="name_uk",
            field=models.CharField(
                max_length=255,
                null=True,
                validators=[django.core.validators.MinLengthValidator(3)],
                verbose_name="Назва",
            ),
        ),
    ]

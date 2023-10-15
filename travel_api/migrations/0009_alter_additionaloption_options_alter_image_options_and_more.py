# Generated by Django 4.2.3 on 2023-10-15 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_api', '0008_alter_image_name_alter_tour_date_end_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionaloption',
            options={'verbose_name_plural': 'Дополнительные опции'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Изображения', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'verbose_name_plural': 'Опции'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='season',
            options={'verbose_name_plural': 'Сезоны'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Статусы'},
        ),
        migrations.AlterModelOptions(
            name='tour',
            options={'ordering': ['name'], 'verbose_name_plural': 'Туры'},
        ),
        migrations.AlterModelOptions(
            name='tourday',
            options={'verbose_name_plural': 'Дни туров'},
        ),
        migrations.AlterModelOptions(
            name='tourdayoption',
            options={'verbose_name_plural': 'Опции дней'},
        ),
        migrations.AlterField(
            model_name='tour',
            name='date_end',
            field=models.DateField(default=datetime.datetime(2023, 10, 15, 18, 3, 45, 1806), verbose_name='Дата кінця'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2023, 10, 15, 18, 3, 45, 1806), verbose_name='Дата почтаку'),
        ),
        migrations.DeleteModel(
            name='TourProgram',
        ),
    ]
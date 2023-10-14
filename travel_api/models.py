from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from datetime import datetime


class Status(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', validators=[MinLengthValidator(3)])
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', validators=[MinLengthValidator(3)])
    description = models.TextField(verbose_name='Описание сезона', blank=True)

    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', validators=[MinLengthValidator(3)])
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.IntegerField(verbose_name='Ціна', validators=[MinValueValidator(1)])
    places = models.IntegerField(verbose_name='Кількість місць (Загальна)', validators=[MinValueValidator(1)])
    free_places = models.IntegerField('Кількість вільних місць', validators=[MinValueValidator(1)])
    is_featured = models.BooleanField(verbose_name='Вибраний?', default=False)
    date_start = models.DateField(verbose_name='Дата почтаку', default=datetime.now())
    date_end = models.DateField(verbose_name='Дата кінця', default=datetime.now())
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.DO_NOTHING, default=1)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, related_name="season", null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def price_with_currency(self):
        return f"₴ {self.price}"
    price_with_currency.short_description = 'Ціна'

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(validators=[MinLengthValidator(3)], max_length=255, verbose_name='Название опции')
    tour = models.ManyToManyField(Tour, related_name='option', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_landmark = models.BooleanField(null=True, default=False, blank=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    icon = models.URLField(max_length=500, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(3)], null=True)
    tour_image = models.ForeignKey(Tour, related_name='images', on_delete=models.CASCADE, primary_key=models.UUIDField())
    aws_url = models.CharField(max_length=255, verbose_name="Ссылка на AWS")
    is_main = models.BooleanField(verbose_name='Главное фото')
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class AdditionalOption(models.Model):
    tour = models.ManyToManyField(Tour, verbose_name='Тур', related_name='adoption', blank=True)
    name = models.CharField(max_length=255, verbose_name='Название', validators=[MinValueValidator(3)])
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.IntegerField(verbose_name='Цена', validators=[MinValueValidator(1)])
    time_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    icon = models.URLField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    tour = models.ForeignKey(Tour, related_name='order', on_delete=models.DO_NOTHING)
    sum = models.IntegerField(verbose_name='Сумма')
    sum_paid = models.IntegerField(verbose_name='Оплаченная сумма')
    code = models.CharField(verbose_name='Код')
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tour.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    place_number = models.IntegerField(verbose_name='Номер места')
    name = models.CharField(verbose_name='Имя')
    surname = models.CharField(verbose_name='Фамилия')
    phone = models.CharField(verbose_name='Номер телефона')
    sum = models.IntegerField(verbose_name='Сумма')
    is_primary_contact = models.BooleanField()
    verification_code = models.IntegerField(verbose_name='Код верификации')

    def __str__(self):
        return self.order


class TourDay(models.Model):
    day = models.CharField(max_length=255, verbose_name='Название дня')
    description = models.TextField(blank=True, verbose_name='Описание дня (необязательно поле)')
    photo = models.URLField(verbose_name='Ссылка на AWS')

    def __str__(self):
        return str(self.day)


class TourDayOption(models.Model):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(3)], verbose_name='Название')
    description = models.TextField(blank=True)
    image_url = models.URLField(null=True)
    date_start = models.DateTimeField(blank=True)
    date_end = models.DateTimeField(blank=True)
    is_landmark = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TourProgram(models.Model):
    tour = models.ManyToManyField(Tour, related_name='program')
    tour_days = models.ManyToManyField(to=TourDay)
    tour_option = models.ManyToManyField(TourDayOption)


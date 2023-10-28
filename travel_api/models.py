from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from datetime import datetime


class Status(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва', validators=[MinLengthValidator(3)])
    description = models.TextField(verbose_name='Опис', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Статуси'


class Season(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва', validators=[MinLengthValidator(3)])
    description = models.TextField(verbose_name='Опис сезону', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Сезони'


class Tour(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва', validators=[MinLengthValidator(3)])
    description = models.TextField(verbose_name='Опис', blank=True)
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

    class Meta:
        verbose_name_plural = 'Тури'
        ordering = ['name']


class Option(models.Model):
    name = models.CharField(validators=[MinLengthValidator(3)], max_length=255, verbose_name='Назва опції')
    tour = models.ManyToManyField(Tour, related_name='option', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_landmark = models.BooleanField(null=True, default=False, blank=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    icon = models.URLField(max_length=500, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Опції'


class Image(models.Model):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(3)], null=True, default='image.png')
    tour_image = models.ForeignKey(to=Tour, related_name='images', on_delete=models.DO_NOTHING, null=True)
    aws_url = models.CharField(max_length=255, verbose_name="Посилання на AWS")
    is_main = models.BooleanField(verbose_name='Головне фото')
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'


class AdditionalOption(models.Model):
    tour = models.ManyToManyField(Tour, verbose_name='Тур', related_name='adoption', blank=True)
    name = models.CharField(max_length=255, verbose_name='Назва', validators=[MinValueValidator(3)])
    description = models.TextField(verbose_name='Опис', blank=True)
    price = models.IntegerField(verbose_name='Ціна', validators=[MinValueValidator(0)])
    time_create = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Дата створення', auto_now=True)
    icon = models.URLField(max_length=255, null=True, verbose_name='Іконка')

    def __str__(self):
        return self.name

    def price_with_currency(self):
        return f"₴ {self.price}"
    price_with_currency.short_description = 'Ціна'

    class Meta:
        verbose_name_plural = 'Додаткові витрати'


class OrderStatus(models.Model):
    status = models.CharField(max_length=255, verbose_name="Статус")
    description = models.CharField(max_length=326, verbose_name="Опис")

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Статусы"
        verbose_name_plural = "Статусы заказов"


class Order(models.Model):
    tour = models.ForeignKey(Tour, related_name='order', on_delete=models.DO_NOTHING)
    sum = models.IntegerField(verbose_name='Сума')
    sum_paid = models.IntegerField(verbose_name='Оплачена сума')
    code = models.CharField(verbose_name='Номер замовлення', unique=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(to=OrderStatus, on_delete=models.DO_NOTHING)
    paytype = models.CharField(max_length=255, verbose_name="Метод оплати", null=True)
    sender_card_mask_2 = models.CharField(max_length=255, verbose_name="Номер карти платника", blank=True, null=True)
    receiver_commission = models.CharField(max_length=255, verbose_name="Liqpay комісія", null=True, blank=True)

    def __str__(self):
        return self.tour.name

    class Meta:
        verbose_name_plural = 'Замовлення'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Замовлення')
    place_number = models.IntegerField(verbose_name='Номер місця')
    name = models.CharField(verbose_name='Імʼя')
    surname = models.CharField(verbose_name='Фамілія')
    phone = models.CharField(verbose_name='Номер телефону', null=True)
    sum = models.IntegerField(verbose_name='Сума')
    is_primary_contact = models.BooleanField(verbose_name='Контакт для звʼязку', default=False)
    verification_code = models.IntegerField(verbose_name='Код верифікації')
    time_create = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name_plural = "Пасажири замовлення"


class TourDay(models.Model):
    day = models.CharField(max_length=255, verbose_name='Назва дня')
    description = models.TextField(blank=True, verbose_name='Опис дня (необязательно поле)')
    photo = models.URLField(verbose_name='Фото')

    def __str__(self):
        return str(self.day)

    class Meta:
        verbose_name_plural = 'Дні турів'


class TourDayOption(models.Model):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(3)], verbose_name='Назва')
    description = models.TextField(blank=True)
    image_url = models.URLField(null=True)
    date_start = models.DateTimeField(blank=True)
    date_end = models.DateTimeField(blank=True)
    is_landmark = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Опції днів'


class TourProgram(models.Model):
    tour = models.ForeignKey(to=Tour, on_delete=models.DO_NOTHING, related_name='program')
    tour_days = models.ForeignKey(to=TourDay, on_delete=models.DO_NOTHING)
    tour_option = models.ForeignKey(to=TourDayOption, on_delete=models.DO_NOTHING)
    order = models.IntegerField(validators=[MinValueValidator(0)], default=1)

    def __str__(self):
        return self.tour.name

    def name(self):
        return self.tour.name

    name.short_description = 'Назва'

    def custom_info(self):
        return f"{self.tour.name} - {self.tour_days.day} - {self.tour_option.name}"

    custom_info.short_description = 'Інформація'

    class Meta:
        verbose_name = 'Програма турів'
        verbose_name_plural = 'Програми турів'

from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание сезона')

    def __str__(self):
        return self.name


class Tour(models.Model):
    tour_id = models.CharField(max_length=255, verbose_name="Пользовательский ID")
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена тура')
    places = models.IntegerField(verbose_name='Общее количество мест')
    free_places = models.IntegerField('Свободные места')
    is_featured = models.BooleanField()
    date_start = models.DateTimeField(verbose_name='Дата старта', blank=True)
    date_end = models.DateTimeField(verbose_name='Дата окончания', blank=True)
    status = models.ManyToManyField(Status, verbose_name='Статус')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="season", null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def price_with_currency(self):
        return f"₴ {self.price}"
    price_with_currency.short_description = 'Ціна'

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название опции')
    tour = models.ManyToManyField(Tour, related_name='option')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_landmark = models.BooleanField(null=True)
    image_url = models.CharField(max_length=255, null=True)
    icon = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    tour_image = models.ForeignKey(Tour, related_name='images', on_delete=models.CASCADE, primary_key=models.UUIDField())
    aws_url = models.CharField(max_length=255, verbose_name="Ссылка на AWS")
    is_main = models.BooleanField(verbose_name='Главное фото')

    def __str__(self):
        return self.aws_url


class AdditionalOption(models.Model):
    tour = models.ManyToManyField(Tour, verbose_name='Тур', related_name='adoption')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    time_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    icon = models.CharField(max_length=255, null=True)

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
    day = models.IntegerField()
    description = models.TextField()
    photo = models.CharField(max_length=255, verbose_name='AWS S3 Фото')

    def __str__(self):
        return str(self.day)


class TourDayOption(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    is_landmark = models.BooleanField()

    def __str__(self):
        return self.name


class TourProgram(models.Model):
    tour = models.ManyToManyField(Tour, related_name='program')
    tour_day = models.ManyToManyField(TourDay)
    tour_option = models.ManyToManyField(TourDayOption)


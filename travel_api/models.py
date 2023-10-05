from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')


class Season(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание сезона')


class Tour(models.Model):
    id = models.CharField(max_length=255, verbose_name="Пользовательский ID", primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена тура')
    places = models.IntegerField(verbose_name='Общее количество мест')
    free_places = models.IntegerField('Свободные места')
    is_featured = models.BooleanField()
    date_start = models.DateTimeField(verbose_name='Дата старта')
    date_end = models.DateTimeField(verbose_name='Дата окончания')
    status = models.ManyToManyField(Status, verbose_name='Статус')
    season = models.ManyToManyField(Season, verbose_name='Сезон')
    time_create = models.DateTimeField()
    time_update = models.DateTimeField()

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название опции')
    tour = models.ManyToManyField(Tour)
    time_create = models.DateTimeField()
    time_update = models.DateTimeField()


class Image(models.Model):
    tour_image = models.ForeignKey(Tour, on_delete=models.CASCADE)
    aws_url = models.CharField(max_length=255, verbose_name="Ссылка на AWS")
    is_main = models.BooleanField(verbose_name='Главное фото')

    def __str__(self):
        return self.aws_url


class AdditionalOption(models.Model):
    tour = models.ManyToManyField(Tour, verbose_name='Тур')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    time_create = models.DateTimeField()
    time_update = models.DateTimeField()


class Order(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.DO_NOTHING)
    sum = models.IntegerField(verbose_name='Сумма')
    sum_paid = models.IntegerField(verbose_name='Оплаченная сумма')
    code = models.CharField(verbose_name='Код')
    time_created = models.DateTimeField()
    time_update = models.DateTimeField()


class OrderItem(models.Model):
    order = models.models.ForeignKey(Order, on_delete=models.CASCADE)
    place_number = models.IntegerField(verbose_name='Номер места')
    name = models.CharField(verbose_name='Имя')
    surname = models.CharField(verbose_name='Фамилия')
    phone = models.CharField(verbose_name='Номер телефона')
    sum = models.IntegerField(verbose_name='Сумма')
    is_primary_contact = models.BooleanField()
    verification_code = models.IntegerField(verbose_name='Код верификации')


class TourDay(models.Model):
    day = models.IntegerField()
    description = models.TextField()
    photo = models.CharField(max_length=255, verbose_name='AWS S3 Фото')


class TourDayOption(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    is_landmark = models.BooleanField()


class TourProgram(models.Model):
    tour = models.ManyToManyField(Tour)

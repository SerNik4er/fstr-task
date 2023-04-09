from django.db import models
from django.contrib.auth.models import User



class Mountaineer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fam = models.CharField(max_length=254, default=None, verbose_name='Фамилия')
    name = models.CharField(max_length=254, default=None, verbose_name='Имя')
    otc = models.CharField(max_length=254, verbose_name='Отчество')
    phone = models.CharField(max_length=30, verbose_name='Номер телефона')
    email = models.EmailField(unique=True, default=None, verbose_name='Электронная почта')

    def __str__(self):
        return f'{self.fam}{self.name}{self.otc}'


class Coords(models.Model):
    latitude = models.FloatField(max_length=13, verbose_name='Широта')
    longitude = models.FloatField(max_length=13, verbose_name='Долгота')
    height = models.FloatField(verbose_name='Высота')


class PerevalAdded(models.Model):
    new = 'NE'
    pending = 'PN'
    accepted = 'AC'
    rejected = 'RJ'
    STAT = [
        (new, 'Новая заявка'),
        (pending, 'Заявка в обработке'),
        (accepted, 'Успешно обработано'),
        (rejected, 'Информация не принята')
    ]
    beautyTitle = models.CharField(max_length=254)
    title = models.CharField(max_length=254, unique=True)
    other_title = models.CharField(max_length=254)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    user = models.ForeignKey(Mountaineer, on_delete=models.CASCADE, related_name='pereval')
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STAT, default=new)
    level_spring = models.CharField(max_length=254, blank=True, verbose_name='Сложность весной')
    level_summer = models.CharField(max_length=254, blank=True, verbose_name='Сложность летом')
    level_autumn = models.CharField(max_length=254, blank=True, verbose_name='Сложность осенью')
    level_winter = models.CharField(max_length=254, blank=True, verbose_name='Сложность зимой')

    def __str__(self):
        return f'id: {self.pk}, title: {self.title}'



class PerevalImages(models.Model):
    title = models.CharField(max_length=254, verbose_name='Название')
    img = models.ImageField(upload_to='photos/%Y/%m/%d')
    date_added = models.DateField(auto_now_add=True, verbose_name='Время добавления')

    def __str__(self):
        return f'id: {self.pk}, title: {self.title}'

    class Meta:
        verbose_name_plural = 'Фотографии'


class PerevalAreas(models.Model):
    id_parent = models.IntegerField(null=True)
    title = models.TextField(null=True)

    class Meta:
        db_table = 'pereval_areas'


class SprActivitiesTypes(models.Model):
    title = models.TextField(null=True)

    class Meta:
        db_table = 'spr_activities_types'
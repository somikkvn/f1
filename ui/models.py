from datetime import datetime

from django.db import models

class Service(models.Model):
    name = models.CharField('Ім\'я', max_length=30)
    email = models.CharField('Email', max_length=50)
    phone = models.CharField('Телефон', max_length=50)
    selected = models.CharField('Категорія реклами', max_length=50)
    info = models.TextField('Додаткова інформація')
    data_public = models.DateField('Дата замовлення', default=datetime.now, blank=True)

    def __str__(self):
        return self.name
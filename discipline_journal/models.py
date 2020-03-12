from django.db import models
from django.urls import reverse
from django import utils
from datetime import datetime
from discipline_journal.choices import PUNISHMENTS, DEPARTMENTS, POSITIONS
import random
import string
from pytils import translit

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class Profile(models.Model):
    surname = models.CharField('Фамилия',max_length=100)
    name = models.CharField('Имя',max_length=100)
    middle_name = models.CharField('Отчество',max_length=100)
    department = models.CharField('Подразделение', choices=DEPARTMENTS, default='ЦДПС Бассоль',max_length=100)
    position = models.CharField('Должность', choices=POSITIONS,default='Сотрудник',max_length=100)
    photo = models.ImageField(upload_to='photo',default='no_photo.jpg',blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return f'{self.surname} {self.name} {self.middle_name}'

    class Meta:
        ordering = ['surname', 'name', 'middle_name']
        verbose_name = 'Профиль сотрудника'
        verbose_name_plural = 'Профили сотрудников'

    def save(self, *args, **kwargs):
        self.slug = translit.slugify(random_string_generator(20))
        super().save(*args, **kwargs)           

class Punishment(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    text = models.CharField('Дисциплинарное взыскание',choices=PUNISHMENTS, max_length=100)
    order = models.CharField('Приказ',max_length=30,blank=True)
    date = models.DateField('Дата',default=utils.timezone.now, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['date']
        verbose_name = 'Дисциплинарное взыскание'
        verbose_name_plural = 'Дисциплинарные взыскания'


        

    

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Kitty(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Имя',
        blank=True,
        null=True
    )
    color = models.CharField(
        max_length=100,
        verbose_name='Цвет'
    )
    age_in_months = models.PositiveSmallIntegerField(
        verbose_name='Возраст в месяцах'
    )
    description = models.TextField(verbose_name='Описание')
    breed = models.ForeignKey(
        to='Breed',
        on_delete=models.CASCADE,
        related_name='kitten',
        null=True
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='kitten',
        verbose_name='Владелец'
    )

    def __str__(self):
        return f'{self.id} {self.name} Цвет: {self.color} ' \
               f'Возраст {self.age_in_months} мес.'


class Breed(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Порода'
    )

    def __str__(self):
        return self.name


class KittyRating(models.Model):
    kitty = models.ForeignKey(
        to='Kitty',
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Рейтинг',
        default=None,
        null=True
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='ratings',
        verbose_name='Владелец',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Оценка {self.rating}'

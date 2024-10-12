from django.db import models
from django.utils import timezone

class Trip(models.Model):
    title = models.CharField(max_length=200, default='Без названия')  # Название поездки
    start_date = models.DateField(default=timezone.now)  # Дата начала поездки
    end_date = models.DateField()  # Дата окончания поездки
    destination = models.CharField(max_length=200)  # Место назначения
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Стоимость поездки
    convenience_rating = models.IntegerField(null=True, blank=True)  # Оценка удобства
    safety_rating = models.IntegerField(null=True, blank=True)  # Оценка безопасности
    population_rating = models.IntegerField(null=True, blank=True)  # Оценка населенности
    vegetation_rating = models.IntegerField(null=True, blank=True)  # Оценка растительности
    image = models.ImageField(upload_to='trip_images/', null=True, blank=True)  # Изображение поездки

    def __str__(self):
        return self.title

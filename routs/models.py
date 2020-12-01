from django.db import models

from trains.models import Train


class Route(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Название маршрута',
                            unique=True)
    
    from_city = models.CharField(max_length=100, verbose_name='Откуда')
    
    to_city = models.CharField(max_length=100, verbose_name='Куда')
    
    trains = models.ManyToManyField(Train, verbose_name='Список поездов',
                                    blank=True)
    
    travel_time = models.IntegerField(verbose_name='Время в пути')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

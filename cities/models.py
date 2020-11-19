from django.db import models


class City(models.Model):
    
    name = models.CharField(max_length=30, unique=True)
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']

    def __str__(self):
        return self.name

from cities.models import City
from django import forms

from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Поезд',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите номер поезда'}))

    from_city = forms.ModelChoiceField(label='Откуда',
                                       queryset=City.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control',
                                                                  'placeholder': 'Откуда'}))

    to_city = forms.ModelChoiceField(label='Куда',
                                     queryset=City.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control',
                                                                'placeholder': 'Куда'}))

    travel_time = forms.IntegerField(label='Время в пути',
                                     widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Время в пути'}))

    class Meta:
        model = Train
        fields = ('name', 'from_city', 'to_city', 'travel_time')

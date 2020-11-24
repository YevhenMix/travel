from cities.models import City
from django.forms import ModelForm, TextInput, CharField


class CityForm(ModelForm):
    name = CharField(label='Город',
                     widget=TextInput(
                         attrs={
                             'class': 'form-control',
                             'placeholder': 'Введите название города'}))

    class Meta:
        model = City
        fields = ('name', )

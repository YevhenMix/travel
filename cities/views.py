from django.shortcuts import render
from cities.models import City


def show_all(request):
    city_lst = City.objects.all()
    context = {'city_lst': city_lst}
    return render(request, 'cities/all_cities.html', context)

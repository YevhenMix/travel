from django.shortcuts import render
from django.views.generic import DetailView

from cities.models import City


def show_all(request):
    city_lst = City.objects.all()
    context = {'city_lst': city_lst}
    return render(request, 'cities/all_cities.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'cities'
    template_name = 'cities/detail.html'

from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from cities.forms import CityForm
from cities.models import City
from django.contrib import messages


def show_all(request):
    city_lst = City.objects.all()
    paginator = Paginator(city_lst, 4)
    page = request.GET.get('page')
    city_lst = paginator.get_page(page)
    context = {'city_lst': city_lst, }
    return render(request, 'cities/all_cities.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'cities'
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:all_cities')
    success_message = 'Город успешно создан!'


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:all_cities')
    success_message = 'Город успешно обновлен!'


class CityDeleteView(SuccessMessageMixin, DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:all_cities')


def delete_city(request, pk):
    if request.method == 'POST':
        city = City.objects.get(id=pk)
        city.delete()
        messages.error(request, 'Город удален!')
    return redirect('cities:all_cities')

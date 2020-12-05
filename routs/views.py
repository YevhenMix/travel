from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView

from routs.forms import RouteForm, RouteModelForm
from routs.models import Route
from routs.utils import get_routes
from trains.models import Train


def home(request):
    form = RouteForm()
    context = {'form': form}
    return render(request, 'routs/home.html', context)


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST or None)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routs/home.html', {'form': form})
        return render(request, 'routs/home.html', context)
    else:
        messages.error(request, 'Создайте маршрут!')
        form = RouteForm()
        context = {'form': form}
        return render(request, 'routs/home.html', context)


def add_route(request):
    if request.method == 'POST':
        data = request.POST
        context = {}
        if data:
            travel_times = data['travel_times']
            from_city = data['from_city']
            to_city = data['to_city']
            trains = data['trains'].split(' ')
            trains_lst = [int(x) for x in trains if x.isalnum()]
            qs = Train.objects.filter(id__in=trains_lst)
            trains_lst = ' '.join(str(i) for i in trains_lst)
            form = RouteModelForm(initial={
                'from_city': from_city,
                'to_city': to_city,
                'travel_times': travel_times,
                'trains': trains_lst,
            })

            route_desc = []
            for tr in qs:
                dsc = f'''Поезд №{tr.name}. Направления {tr}. Время в пути {tr.travel_time}'''
                route_desc.append(dsc)

            context = {'form': form, 'desc': route_desc, 'from_city': from_city, 'to_city': to_city,
                       'travel_times': travel_times}

        return render(request, 'routs/create.html', context)
    else:
        messages.error(request, 'Невозможно сохранить несуществующий маршрут!')
        return redirect('/')


def save_route(request):
    if request.method == 'POST':
        data = request.POST
        context = {}
        if data:
            name = data['name']
            travel_times = data['travel_times']
            from_city = data['from_city']
            to_city = data['to_city']
            trains = data['trains'].split(' ')
            print(trains)
            trains_lst = [int(x) for x in trains if x.isalnum()]
            print(trains_lst)
            qs = Train.objects.filter(id__in=trains_lst)
            print(qs)
            route = Route(name=name, from_city=from_city,
                          to_city=to_city, travel_time=travel_times)
            route.save()
            route.trains.set(qs)
            messages.success(request, 'Маршрут был усешно создан')
            return redirect('/')
        return render(request, 'routs/create.html', context)
    else:
        messages.error(request, 'Неозможно сохранить несуществующий маршрут')
        return redirect('/')


class RouteDetailView(DetailView):
    queryset = Route.objects.all()
    template_name = 'routs/detail.html'


class RouteListView(ListView):
    queryset = Route.objects.all()
    template_name = 'routs/list.html'
    paginate_by = 2


class RouteDeleteView(SuccessMessageMixin, DeleteView):
    model = Route
    template_name = 'routs/delete.html'
    success_url = reverse_lazy('all_routs')


def delete_rout(request, pk):
    if request.method == 'POST':
        rout = Route.objects.get(id=pk)
        rout.delete()
        messages.error(request, 'Маршрут удален!')
    return redirect('all_routs')

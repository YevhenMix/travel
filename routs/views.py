from django.shortcuts import render, redirect
from django.contrib import messages
from routs.forms import RouteForm
from routs.utils import get_routes


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

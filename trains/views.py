from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from trains.forms import TrainForm
from trains.models import Train


def home(request):
    trains_lst = Train.objects.all()
    paginator = Paginator(trains_lst, 5)
    page = request.GET.get('page')
    trains_lst = paginator.get_page(page)
    context = {'trains': trains_lst, }
    return render(request, 'trains/home.html', context)


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'
    context_object_name = 'trains'


class TrainCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Поезд успешно создан!'
    login_url = '/users/login/'


class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Поезд успешно обновлен!'
    login_url = '/users/login/'


class TrainDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Train
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:home')
    login_url = '/users/login/'


def delete_train(request, pk):
    if request.method == 'POST':
        train = Train.objects.get(id=pk)
        train.delete()
        messages.error(request, 'Поезд удален!')
    return redirect('trains:home')




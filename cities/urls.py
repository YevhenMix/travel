from django.urls import path
from cities.views import show_all, CityDetailView

app_name = 'cities'

urlpatterns = [
    path('all_cities/', show_all, name='all_cities'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
]

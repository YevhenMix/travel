from django.urls import path
from cities.views import show_all, CityDetailView, CityCreateView, CityUpdateView, CityDeleteView, delete_city

app_name = 'cities'

urlpatterns = [
    path('all_cities/', show_all, name='all_cities'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('create/', CityCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    path('delete_cor/<int:pk>/', delete_city, name='delete_cor'),
]

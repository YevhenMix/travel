"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from routs.views import home, find_routes, add_route, save_route, RouteListView, RouteDetailView, RouteDeleteView, delete_rout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cities/', include('cities.urls', 'cities')),
    path('trains/', include('trains.urls', 'trains')),
    path('users/', include('users.urls', 'users')),
    path('find/', find_routes, name='find_routes'),
    path('add_rout/', add_route, name='add_route'),
    path('save_route/', save_route, name='save_route'),
    path('all_routs/', RouteListView.as_view(), name='all_routs'),
    path('route_detail/<int:pk>', RouteDetailView.as_view(), name='route_detail'),
    path('delete_rout/<int:pk>', RouteDeleteView.as_view(), name='delete_rout'),
    path('delete_rout_cor/<int:pk>', delete_rout, name='delete_rout_cor'),
]

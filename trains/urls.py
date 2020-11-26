from django.urls import path
from trains.views import home, TrainCreateView, TrainUpdateView, TrainDeleteView, TrainDetailView ,delete_train

app_name = 'trains'

urlpatterns = [
    path('', home, name='home'),
    path('create/', TrainCreateView.as_view(), name='create'),
    path('detail/<int:pk>', TrainDetailView.as_view(), name='detail'),
    path('update/<int:pk>', TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TrainDeleteView.as_view(), name='delete'),
    path('delete_cor/<int:pk>', delete_train, name='delete_cor'),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CarsView.as_view(), name='cars'),
    path('<slug:slug>/', views.CarsDetailView.as_view(), name='car_detail'),
]
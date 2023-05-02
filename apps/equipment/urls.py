from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProductsView.as_view(), name='products'),
]
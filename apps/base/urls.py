from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('ready/', views.ReadyView.as_view(), name='ready'),
    path('about/', views.AboutView.as_view(), name='about'),

]

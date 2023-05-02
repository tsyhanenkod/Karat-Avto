from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ServicesView.as_view(), name='services'),
    path('guarantee/', views.GuaranteeView.as_view(), name='guarantee'),
    path('lizing/', views.LizingView.as_view(), name='lizing'),
    path('credit/', views.CreditView.as_view(), name='credit'),
    path('insurance/', views.InsuranceView.as_view(), name='insurance'),
    path('reregistration/', views.ReregistrationView.as_view(), name='reregistration'),
    path('car_on_commission/', views.CarOnCommissionView.as_view(), name='car_on_commission'),
    path('equipment/', include('equipment.urls')),
]
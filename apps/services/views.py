from django.shortcuts import render
from django.views import View
# from ..equipment.models import *

class ServicesView(View):
    def get(self, request):
        context={}
        return render(request, 'services/services.html', context)


class GuaranteeView(View):
    def get(self, request):
        context = {}
        return render(request, 'services/guarantee.html', context)


class LizingView(View):
    def get(self, request):
        context = {}
        return render(request, 'services/lizing.html', context)


class CreditView(View):
    def get(self, request):
        context = {}
        return render(request, 'services/credit.html', context)


class InsuranceView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'services/insurance.html', context)


class ReregistrationView(View):
    def get(self, request):
        context = {}
        return render(request, 'services/reregistration.html', context)


class EquipmentView(View):
    def get(self, request):
        products = 'pass'

        context = {
            'products':products,
        }
        return render(request, 'services/equipment.html', context)


class CarOnCommissionView(View):
    def get(self, request):
        context = {}
        return render(request, 'services/car_on_commission.html', context)

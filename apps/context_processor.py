from django.shortcuts import render, redirect
from django.views.generic.base import View
from base.models import *
from cars.models import *
from services.models import *
from complect.models import *
from equipment.models import *
from django.utils import translation
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings

def store_dynamic(request):
    car_category = Category.objects.all()
    car_mark = CarMark.objects.all()
    car_model = CarModel.objects.all()
    car_engine_type = EngineTypes.objects.all()
    car_transmission = Transmission.objects.all()
    car_color = Colors.objects.all()
    service = Service.objects.all()
    banner = BannerList.objects.all()

    context = {
        'car_category': car_category,
        'car_mark':car_mark,
        'car_model':car_model,
        'car_engine_type':car_engine_type,
        'car_transmission':car_transmission,
        'car_color':car_color,
        'service':service,
        'banner':banner,
    }
    return context

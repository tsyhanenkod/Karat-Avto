import os

from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, View
from .models import *
from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.mail import send_mail
import os
from complect.models import *


class CarsView(View):
    def get(self, request):
        car = Car.objects.filter(draft=False)
        params = {
            'category': self.request.GET.get('category'),
            'mark': self.request.GET.get('mark'),
            'model': self.request.GET.get('model'),
            'color': self.request.GET.get('color'),
            'engine_type': self.request.GET.get('enginet'),
            'transmission': self.request.GET.get('transmission'),
            'min_year': self.request.GET.get('min_year'),
            'max_year': self.request.GET.get('max_year'),
            'min_price': self.request.GET.get('min_price'),
            'max_price': self.request.GET.get('max_price'),
        }

        q_objects = Q(draft=False)
        for key, value in params.items():
            if value:
                if key == 'min_year':
                    q_objects &= Q(year__gte=value)
                elif key == 'max_year':
                    q_objects &= Q(year__lte=value)
                elif key == 'min_price':
                    q_objects &= Q(price__gte=value)
                elif key == 'max_price':
                    q_objects &= Q(price__lte=value)
                else:
                    q_objects &= Q(**{f"{key}__url": value})

        car = car.filter(q_objects)

        context = {
            'car': car,
            'params': params
        }

        return render(request, 'cars/cars.html', context)

class CarsDetailView(View):
    def get(self, request, slug):

        car = Car.objects.get(url=slug)
        drive_unit = DriveUnit.objects.all()

        char_category = Charcategory.objects.all()
        complects = Complect.objects.all()
        char = Char.objects.all()
        value = Values.objects.all()
        complect_transmissions = Prices.objects.all()

        context = {
            "car": car,
            "drive_unit": drive_unit,
            "char_category": char_category,
            "complects": complects,
            "char": char,
            "value": value,
            'complect_transmissions':complect_transmissions,
        }

        return render(request, 'cars/car_detail.html', context)

    def post(self, request, slug):
        car = Car.objects.get(url=slug)
        drive_unit = DriveUnit.objects.all()
        price = intcomma(car.price)

        char_category = Charcategory.objects.all()
        complects = Complect.objects.all()
        char = Char.objects.all()
        value = Values.objects.all()
        complect_transmissions = Prices.objects.all()

        context = {
            "car": car,
            "drive_unit": drive_unit,
            "char_category": char_category,
            "complects": complects,
            "char": char,
            "value": value,
            'complect_transmissions': complect_transmissions,
        }

        if request.method == 'POST':
            name = request.POST.get('form-name'),
            email = request.POST.get('form-email'),
            tel = request.POST.get('form-tel'),
            msg = request.POST.get('form-msg'),
            check = request.POST.get('form-check'),

            print(name[0], email[0], tel[0], msg[0], check[0])

            if str(check[0]) == 'on':
                check = 'Так'
            elif str(check[0]) == 'None':
                check = 'Ні'
            else:
                check = check

            my_mail = f"{os.environ.get('ORDERING_MAIL')}"

            send_mail(
                f'Заявка на {car} від {str(name[0])}',
                str(f"Автомобіль: {car}\nІм'я: {name[0]}\nE-mail: {email[0]}\nТелефон: {tel[0]}\nЗворотній дзвінок: {check}\n\nПовідомлення: \n{msg[0]}"),
                'youremail@example.com',
                [str(my_mail)],
                fail_silently=False,
            )

            # Рендеринг страницы после отправки письма
            return render(request, 'cars/car_detail.html', context, complect_context)
        else:
            # Рендеринг страницы с формой
            return render(request, 'cars/car_detail.html', context, complect_context)

        return render(request, 'cars/car_detail.html', context, complect_context)
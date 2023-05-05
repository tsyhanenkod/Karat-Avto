import os
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, View
from .models import *
from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.mail import send_mail
import os
from complect.models import *
from django.core.paginator import Paginator, EmptyPage
from django.utils.translation import activate, get_language


class CarsView(View):
    def get(self, request):
        car = Car.objects.filter(draft=False)
        language = get_language()

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
        if language == 'en':
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
        elif language == 'uk':
            for key, value in params.items():
                if value:
                    if key == 'min_year':
                        q_objects &= Q(year__gte=value)
                    elif key == 'max_year':
                        q_objects &= Q(year__lte=value)
                    elif key == 'min_price':
                        q_objects &= Q(price_ua__gte=value)
                    elif key == 'max_price':
                        q_objects &= Q(price_ua__lte=value)
                    else:
                        q_objects &= Q(**{f"{key}__url": value})

        car = car.filter(q_objects)
        paginator = Paginator(car, 18)
        page_number = request.GET.get("page")
        try:
            page_obj = paginator.get_page(page_number)
        except EmptyPage:
            page_obj = paginator.get_page(page_number)

        context = {
            # 'car': car,
            'params': params,
            'page_obj':page_obj,
        }

        return render(request, 'cars/cars.html', context)


    # def get(self, request):
    #     car = Car.objects.all()
    #     paginator = Paginator(car, 1)  # Show 25 contacts per page.
    #
    #     page_number = request.GET.get("page")
    #     page_obj = paginator.get_page(page_number)
    #     return render(request, "cars/cars.html", {"page_obj": page_obj})


class CarsDetailView(View):
    def get(self, request, slug):

        car = Car.objects.get(url=slug)
        drive_unit = DriveUnit.objects.all()

        char_category = Charcategory.objects.all()
        complects = Complect.objects.filter(car=car)
        char = Char.objects.select_related('char_category')
        value = Values.objects.select_related('complectation').select_related('char')
        complect_transmissions = Prices.objects.all()
        print(complects)
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
        complects = Complect.objects.filter(car=car)
        char = Char.objects.select_related('char_category')
        value = Values.objects.select_related('complectation').select_related('char')
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
            name = request.POST.get('form-name')
            email = request.POST.get('form-email')
            tel = request.POST.get('form-tel')
            msg = request.POST.get('form-msg')
            check = request.POST.get('form-check')

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
            return redirect('ready')
        else:
            # Рендеринг страницы с формой
            return redirect('ready')

        return redirect('ready')

import os
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
import environ

env = environ.Env()



class HomeView(View):
    def get(self, request):
        API_KYIV = f"{os.environ.get('KYIV_GOOGLEMAPS_API')}"
        API_VISHGOROD = f"{os.environ.get('VISHGOROD_GOOGLEMAPS_API')}"

        context = {
            'apikyiv': API_KYIV,
            'apivishgorod': API_VISHGOROD,
        }
        return render(request, 'base/home.html', context)


class ContactsView(View):
    def get(self, request):
        API_KYIV = f"{env('KYIV_GOOGLEMAPS_API')}"
        API_VISHGOROD = f"{env('VISHGOROD_GOOGLEMAPS_API')}"

        context = {
            'apikyiv': API_KYIV,
            'apivishgorod': API_VISHGOROD,
        }
        return render(request, 'base/contacts.html', context)


    def post(self, request):

        context = {}

        if request.method == 'POST':
            name = request.POST.get('cotacts-name')
            email = request.POST.get('cotacts-email')
            tel = request.POST.get('cotacts-tel')
            msg = request.POST.get('cotacts-msg')
            check = request.POST.get('cotacts-ringup')


            print(check)
            if check:
                check = 'Так'
            if not check:
                check = 'Ні'

            my_mail = f"{env('ORDERING_MAIL')}"

            send_mail(
                f'Повідомлення від {name} з контактної форми',
                str(f"Ім'я: {name}\nE-mail: {email}\nТелефон: {tel}\nЗворотній дзвінок: {check}\n\nПовідомлення: \n{msg}"),
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


class AboutView(View):
    def get(self, request):
        context = {}
        return render(request, 'base/about.html', context)


class ReadyView(View):
    def get(self, request):
        context = {}
        return render(request, 'base/ready.html', context)
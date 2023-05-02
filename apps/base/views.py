import os
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail


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
        API_KYIV = f"{os.environ.get('KYIV_GOOGLEMAPS_API')}"
        API_VISHGOROD = f"{os.environ.get('VISHGOROD_GOOGLEMAPS_API')}"

        context = {
            'apikyiv': API_KYIV,
            'apivishgorod': API_VISHGOROD,
        }
        return render(request, 'base/contacts.html', context)


    def post(self, request):

        context = {}

        if request.method == 'POST':
            name = request.POST.get('cotacts-name'),
            email = request.POST.get('cotacts-email'),
            tel = request.POST.get('cotacts-tel'),
            msg = request.POST.get('cotacts-msg'),
            check = request.POST.get('contacts-rignup'),

            print(name[0], email[0], tel[0], msg[0], check[0])

            if str(check[0]) == 'on':
                check = 'Так'
            elif str(check[0]) == 'None':
                check = 'Ні'
            else:
                check = check

            my_mail = f"{os.environ.get('ORDERING_MAIL')}"

            send_mail(
                f'Повідомлення від {str(name[0])} з контактної форми',
                str(f"Ім'я: {name[0]}\nE-mail: {email[0]}\nТелефон: {tel[0]}\nЗворотній дзвінок: {check}\n\nПовідомлення: \n{msg[0]}"),
                'youremail@example.com',
                [str(my_mail)],
                fail_silently=False,
            )
            # Рендеринг страницы после отправки письма
            return render(request, 'base/contacts.html', context)
        else:
            # Рендеринг страницы с формой
            return render(request, 'base/contacts.html', context)

        return render(request, 'base/contacts.html', context)

class AboutView(View):
    def get(self, request):
        context = {}
        return render(request, 'base/about.html', context)

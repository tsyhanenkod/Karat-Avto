from django.shortcuts import render
from django.views import View
from .models import *

class ProductsView(View):
    def get(self, request):
        products = Product.objects.filter(draft=False)

        context={
            'products':products,
        }

        return render(request, 'equipment/products.html', context)


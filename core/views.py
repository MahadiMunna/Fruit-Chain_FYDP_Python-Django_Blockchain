from django.shortcuts import render
from fruit.models import FruitModel
from django.views.generic import DetailView
# Create your views here.
def home(request):
    data = FruitModel.objects.filter(flash_sale=False)
    flashsale = FruitModel.objects.filter(flash_sale=True)
    return render(request, 'home.html', {'data':data, 'flashsale':flashsale })


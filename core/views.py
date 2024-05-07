from django.shortcuts import render
from fruit.models import FruitModel
from django.views.generic import DetailView
# Create your views here.
def home(request):
    data = FruitModel.objects.filter(stocked_out=False, flash_sale=False)
    return render(request, 'home.html', {'data':data})


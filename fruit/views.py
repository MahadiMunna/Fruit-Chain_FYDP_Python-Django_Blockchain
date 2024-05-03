from django.shortcuts import render
from django.views.generic import DetailView
from fruit.models import FruitModel

# Create your views here.
class DetailFruitView(DetailView):
    model = FruitModel
    pk_url_kwarg = 'id'
    template_name = 'fruit_details.html'
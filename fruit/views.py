from django.shortcuts import render, redirect
from django.views.generic import DetailView
from fruit.models import FruitModel
from .forms import PostForm
from django.contrib import messages

# Create your views here.
class DetailFruitView(DetailView):
    model = FruitModel
    pk_url_kwarg = 'id'
    template_name = 'fruit_details.html'

def add_fruit(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            name = post_form.cleaned_data.get("name")
            description = post_form.cleaned_data.get("description")
            location = post_form.cleaned_data.get("location")
            supply_date = post_form.cleaned_data.get("supply_date")
            price = post_form.cleaned_data.get("price")
            image = post_form.cleaned_data.get("image")
            FruitModel.objects.create(
                name=name,
                description=description,
                location=location,
                supply_date=supply_date,
                price=price,
                image=image,
            )
            messages.success(request,'Your sell post added successfully')
            return redirect('home')
    else:
        post_form = PostForm()
    return render(request, 'add_fruit.html', {'form': post_form, 'type':'Add fruit sell post'})

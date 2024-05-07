from django.shortcuts import render, redirect
from django.views.generic import DetailView
from fruit.models import FruitModel, Vendor
from django.contrib import messages
from .forms import FruitForm, VendorForm

# Create your views here.
class DetailFruitView(DetailView):
    model = FruitModel
    pk_url_kwarg = 'id'
    template_name = 'fruit_details.html'


def add_fruit(request):
    vendors = Vendor.objects.all()
    if request.method == 'POST':
        fruit_form = FruitForm(request.POST, request.FILES)

        if fruit_form.is_valid():
            name = fruit_form.cleaned_data.get("name")
            image = fruit_form.cleaned_data.get("image")
            description = fruit_form.cleaned_data.get("description")
            location = fruit_form.cleaned_data.get("location")
            vendor = fruit_form.cleaned_data.get("vendor")
            supply_date = fruit_form.cleaned_data.get("supply_date")
            price = fruit_form.cleaned_data.get("price")
            discount = fruit_form.cleaned_data.get("discount")

            
            FruitModel.objects.create(
                name=name,
                description=description,
                location=location,
                supply_date=supply_date,
                price=price,
                image=image,
                vendor=vendor,
                discount=discount
            )
            messages.success(request, 'New fruit added successfully!')
            return redirect('home')
    else:
        fruit_form = FruitForm()

        return render(request, 'add_fruit.html', {'form': fruit_form, 'vendors': vendors})
    return render(request, 'add_fruit.html', {'form': fruit_form, 'vendors': vendors})

def add_vendor(request):
    vendor_form = VendorForm()
    if request.method == 'POST':
        vendor_form = VendorForm(request.POST, request.FILES)
        if vendor_form.is_valid():
            vendor_name = vendor_form.cleaned_data.get("vendor_name")
            NID_number = vendor_form.cleaned_data.get("NID_number")
            phone_number = vendor_form.cleaned_data.get("phone_number")
            address = vendor_form.cleaned_data.get("address")

            Vendor.objects.create(
                vendor_name=vendor_name,
                NID_number=NID_number,
                phone_number=phone_number,
                address=address,
            )
            messages.success(request, 'New vendor added successfully. Add more vendor!')
            return redirect('add_vendor')
        else:
            return render(request, 'add_vendor.html', {'form': vendor_form })
    return render(request, 'add_vendor.html', {'form': vendor_form })
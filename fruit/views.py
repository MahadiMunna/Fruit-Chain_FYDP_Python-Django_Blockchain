from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import DetailView
from fruit.models import FruitModel, Vendor, FavouriteFruit, Wishlist
from django.contrib import messages
from .forms import FruitForm, VendorForm, CommentForm

from django.contrib.auth.decorators import login_required

# Create your views here.
def available_fruits(request):
    data = FruitModel.objects.filter(stocked_out=False)
    return render(request, 'fruits.html', {'data':data })

class DetailFruitView(DetailView):
    model = FruitModel
    pk_url_kwarg = 'id'
    template_name = 'fruit_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        name = self.request.user.account
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = name
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

@login_required
def add_fruit(request):
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

        return render(request, 'add_fruit.html', {'form': fruit_form})
    return render(request, 'add_fruit.html', {'form': fruit_form})


class EditFruitView(View):
    template_name = 'edit_fruit.html'
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        fruit_id = kwargs.get(self.pk_url_kwarg)
        fruit_instance = get_object_or_404(FruitModel, id=fruit_id)
        form = FruitForm(instance=fruit_instance)
        return render(request, self.template_name, {'form': form, 'fruit_instance': fruit_instance})

    def post(self, request, *args, **kwargs):
        fruit_id = kwargs.get(self.pk_url_kwarg)
        fruit_instance = get_object_or_404(FruitModel, id=fruit_id)
        form = FruitForm(request.POST, request.FILES, instance=fruit_instance)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Fruit post updated successfully!')
            return redirect('home')
        return render(request, self.template_name, {'form': form})

@login_required
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

@login_required
def make_stocked_out(request, id):
    fruit = get_object_or_404(FruitModel, id=id)
    fruit.stocked_out = True
    fruit.flash_sale = False
    fruit.save()
    return redirect('home')

@login_required
def archive_fruits(request):
    data = FruitModel.objects.filter(stocked_out=True)
    return render(request, 'archive_fruits.html', {'data':data})

@login_required
def move_to_regular(request, id):
    fruit = get_object_or_404(FruitModel, id=id)
    fruit.stocked_out = False
    fruit.save()
    return redirect('archive')

@login_required
def remove_fruit(request, id):
    fruit = get_object_or_404(FruitModel, id=id)
    fruit.delete()
    return redirect('archive')

@login_required
def add_to_flash_sale(request, id):
    fruit = get_object_or_404(FruitModel, id=id)
    fruit.flash_sale = True
    fruit.save()
    return redirect('home')

@login_required
def flash_sale_fruits(request):
    data = FruitModel.objects.filter(flash_sale=True)
    return render(request, 'flash_sale.html', {'data':data})

@login_required
def make_regular_sale(request, id):
    fruit = get_object_or_404(FruitModel, id=id)
    fruit.flash_sale = False
    fruit.save()
    return redirect('flash_sale_fruits')

@login_required
def add_to_favorites(request, id):
    fruit = get_object_or_404(FruitModel, id=id)
    FavouriteFruit.objects.get_or_create(user=request.user, fruit=fruit)
    return redirect('home')

@login_required
def favourite_fruits(request):
    favorite_fruits = FavouriteFruit.objects.filter(user=request.user)
    return render(request, 'favourite_fruits.html', {'favorite_fruits': favorite_fruits})

@login_required
def remove_from_favourites(request, id):
    favorite_fruit = get_object_or_404(FavouriteFruit, id=id, user=request.user)
    favorite_fruit.delete()
    return redirect('favourite')

@login_required
def add_to_wishlist(request, id):
    fruit = get_object_or_404(FruitModel, id=id)
    Wishlist.objects.get_or_create(user=request.user, fruit=fruit)
    return redirect('home')

@login_required
def wishlist(request):
    fruits = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'fruits': fruits})

@login_required
def remove_from_wishlist(request, id):
    wish_fruit = get_object_or_404(Wishlist, id=id, user=request.user)
    wish_fruit.delete()
    return redirect('wishlist')
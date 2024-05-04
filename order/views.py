from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from fruit.models import FruitModel
from .models import Cart, Order
from django.contrib import messages

# Create your views here.
def add_to_cart(request, pk):
    item = get_object_or_404(FruitModel, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_items.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.success(request,f'{item.name} Successfully added to cart!')
            referer_url = request.META.get('HTTP_REFERER', '/')
            return HttpResponseRedirect(referer_url)
        else:
            order.order_items.add(order_item[0])
            messages.success(request,f'{item.name} Successfully added to cart!')
            referer_url = request.META.get('HTTP_REFERER', '/')
            return HttpResponseRedirect(referer_url)
    else:
        order = Order(user=request.user)
        order.save()
        order.order_items.add(order_item[0])
        messages.success(request,f'{item.name} Successfully added to cart!')
        referer_url = request.META.get('HTTP_REFERER', '/')
        return HttpResponseRedirect(referer_url)

def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        context = {
            'carts':carts,
            'order':order
        }
        return render(request, 'cart.html', context)
    else:
        return render(request, 'cart.html')

def remove_from_cart(request, pk):
    item = get_object_or_404(FruitModel, pk=pk)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if orders.exists():
        order = orders[0]
        if order.order_items.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            order.order_items.remove(order_item)
            order_item.delete()
            messages.warning(request,f'{item.name} removed from cart!')
            return redirect('cart')
        else:
            return redirect('cart')
    else:
        return redirect('cart')

def increase_decrease(request, pk, type):
    item = get_object_or_404(FruitModel, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.order_items.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if type=='increase':
                if order_item.quantity >= 1:
                    order_item.quantity += 1
                    order_item.save()
                    return redirect('cart')
            elif type=='decrease':
                if order_item.quantity > 1:
                    order_item.quantity -= 1
                    order_item.save()
                    return redirect('cart')
                else:
                    order.order_items.remove(order_item)
                    order_item.delete()
                    messages.warning(request,f'{item.name} removed from cart!')
                    return redirect('cart')
        else:
            return redirect('cart')
    else:
        return redirect('cart')
    
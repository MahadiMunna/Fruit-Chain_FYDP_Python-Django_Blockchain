from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
    path('cart-view/', views.cart_view, name='cart'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart , name='remove'),
    path('increase-decrease/<int:pk>/<type>', views.increase_decrease , name='increase-decrease'),
]
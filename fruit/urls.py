from django.urls import path
from . import views

urlpatterns = [
    path('fruit_details/<int:id>/', views.DetailFruitView.as_view(), name='details'),
    path('add_fruit', views.add_fruit, name='add_fruit'),
    path('add_vendor', views.add_vendor, name='add_vendor'),
]
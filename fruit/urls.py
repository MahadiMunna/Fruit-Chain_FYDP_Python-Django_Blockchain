from django.urls import path
from . import views

urlpatterns = [
    path('fruit_details/<int:id>/', views.DetailFruitView.as_view(), name='details'),

    path('add_fruit', views.add_fruit, name='add_fruit'),
    path('edit_fruit/<int:id>/', views.EditFruitView.as_view(), name='edit_fruit'),
    path('add_vendor', views.add_vendor, name='add_vendor'),

    path('stocked_out/<int:id>/', views.make_stocked_out, name='stocked_out'),
    path('archive_fruits/', views.archive_fruits, name='archive'),
    path('move_to_regular/<int:id>/', views.move_to_regular, name='move_to_regular'),

    path('flash_sale/<int:id>/', views.add_to_flash_sale, name='flash_sale'),
    path('flash_sale/', views.flash_sale_fruits, name='flash_sale_fruits'),
    path('regular_sale/<int:id>/', views.make_regular_sale, name='regular_sale'),

    path('favourite/<int:id>/', views.add_to_favorites, name='add_to_favourite'),
    path('favourite_fruits/', views.favourite_fruits, name='favourite'),
    path('remove_favourite/<int:id>/', views.remove_from_favourites, name='remove_favourite'),

    
]
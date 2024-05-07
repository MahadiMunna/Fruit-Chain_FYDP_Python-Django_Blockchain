from django.contrib import admin
from .models import FruitModel, Vendor
# Register your models here.

admin.site.register(Vendor)
admin.site.register(FruitModel)
from django.contrib import admin
from .models import UserAccount, VendorAccount
# Register your models here.
admin.site.register(UserAccount)
admin.site.register(VendorAccount)
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='./profile-images/uploads/', blank=True, null=True)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class VendorAccount(models.Model):
    user = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)
    NID_number = models.CharField(max_length=17)
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
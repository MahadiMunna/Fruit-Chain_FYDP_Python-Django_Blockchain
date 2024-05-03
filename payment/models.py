from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BillingAddress(models.Model):
    user = models.ForeignKey(User,related_name='address', on_delete=models.CASCADE)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} - {self.city}'
    
    def form_validation(self):
        field_names = [f.name for f in self._meta.get_fields()]
        for field_name in field_names:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False
            return True

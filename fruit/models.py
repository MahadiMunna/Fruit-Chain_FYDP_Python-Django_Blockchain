from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100)
    NID_number = models.CharField(max_length=17)
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.vendor_name}"
class FruitModel(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='./fruit-images/', blank=True, null=True)
    description=models.TextField()
    location=models.CharField(max_length=100)
    vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)
    supply_date=models.DateField()
    price=models.DecimalField(max_digits=8, decimal_places=2)
    discount=models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    timestamp=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} from {self.location}"


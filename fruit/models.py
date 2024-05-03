from django.db import models

# Create your models here.
class FruitModel(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='./fruit-images/', blank=True, null=True)
    description=models.TextField()
    location=models.CharField(max_length=100)
    supply_date=models.DateField()
    price=models.DecimalField(max_digits=8, decimal_places=2)
    timestamp=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} from {self.location}"
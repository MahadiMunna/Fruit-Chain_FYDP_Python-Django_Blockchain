from django.db import models
from django.contrib.auth.models import User

from fruit.models import FruitModel

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    item = models.ForeignKey(FruitModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item} - {self.quantity}"
    
    def get_total(self):
        if self.item.discount > 0:
            total = float(self.item.get_discounted_price())*self.quantity
            return format(total, '0.2f')
        else:
            total = self.item.price*self.quantity
            return format(total, '0.2f')


PAYMENT_METHOD = (
    ('Cash on delivery', 'Cash on delivery'),
    ('SSLCOMMERZ', 'SSLCOMMERZ'),
)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=100, blank=True, null=True)
    orderId = models.CharField(max_length=100, blank=True, null=True)
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHOD, default='Cash on delivery')

    def get_totals(self):
        total = 0
        for order_item in self.order_items.all():
            total += float(order_item.get_total())

        return format(total, "0.2f")
    
    def __str__(self):
        order_status = 'Order Pending'
        if self.ordered:
            order_status = 'Ordered'
        return f'{self.user.first_name}-{order_status}'
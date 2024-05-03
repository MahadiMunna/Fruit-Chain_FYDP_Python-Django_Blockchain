from django import forms
from .models import BillingAddress
from order.models import Order

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = '__all__'

        widgets = {
          'address': forms.Textarea(attrs={'rows':3}),
        }

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['payment_method',]
from django import forms
from .models import FruitModel, Vendor

class FruitForm(forms.ModelForm):
    class Meta:
        model=FruitModel
        fields= '__all__'

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields= '__all__'


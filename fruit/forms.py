from django import forms
from .models import FruitModel

class PostForm(forms.ModelForm):
    class Meta:
        model=FruitModel
        fields= '__all__'
        widgets = {
          'description': forms.Textarea(attrs={'rows':3}),
          'supply_date': forms.DateInput({'type':'date'})
        }

from django import forms
from .models import FruitModel, Vendor, Comment

class FruitForm(forms.ModelForm):
    class Meta:
        model=FruitModel
        fields= '__all__'

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields= '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
          'comment': forms.Textarea(attrs={'rows':3}),
        }
from django import forms
from products.models import Category



class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
        }
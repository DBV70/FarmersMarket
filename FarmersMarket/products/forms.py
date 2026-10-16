from django import forms
from FarmersMarket.products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    widgets = {
        'price': forms.NumberInput(attrs={'step': '0.01'}),
        'quantity': forms.NumberInput(attrs={'step': '1'}),
        'image': forms.FileInput(),
        'description': forms.Textarea(),
        'category': forms.Select(),
        'unit': forms.Select(),
        'producer': forms.Select(),
        'expiry_date': forms.DateInput(attrs={'type': 'date'}),

    }

    labels = {
        'name': 'Producer Name:',
        'price': 'Price:',
        'quantity': 'Quantity:',
        'image': 'Image:',
        'description': 'Description:',
        'category': 'Category:',
        'unit': 'Unit:',
        'producer': 'Producer:',
        'expiry_date': 'Expiry Date:',
    }

class ProductCreateForm(ProductForm):
    pass

class ProductUpdateForm(ProductForm):
    pass

class ProductDeleteForm(ProductForm):
    pass

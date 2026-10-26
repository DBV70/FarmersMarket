from django import forms
from FarmersMarket.products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter product name'}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'}),
            'quantity': forms.NumberInput(attrs={'step': '1'}),
            'image': forms.FileInput(),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Product description...'}),
            'category': forms.Select(),
            'unit': forms.Select(),
            'producer': forms.Select(),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

        labels = {
            'name': 'Product Name:',
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

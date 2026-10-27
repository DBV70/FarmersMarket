from django import forms
from FarmersMarket.common.forms import SearchForm
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

        help_texts = {
            'price': 'Enter the price of the product.',
            'quantity': 'Enter the quantity of the product.',
            'image': 'Upload an image of the product.',
            'category': 'Select the category of the product.',
            'unit': 'Select the unit of measurement.',
            'producer': 'Select the producer of the product.',
            'expiry_date': 'Enter the expiry date of the product.',
        }

        error_messages = {
            'name': {'required': 'Please enter the product name.'},
            'price': {'required': 'Please enter the product price.'},
            'quantity': {'required': 'Please enter the product quantity.'},
            'category': {'required': 'Please select a product category.'},
            'unit': {'required': 'Please select a unit of measurement.'},
            'producer': {'required': 'Please select a producer.'},
        }

class ProductCreateForm(ProductForm):
    pass

class ProductUpdateForm(ProductForm):
    pass

class ProductDeleteForm(ProductForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['name'].disabled = True
            self.fields['description'].disabled = True

    class Meta(ProductForm.Meta):
        exclude = ['price', 'quantity', 'category', 'unit', 'producer', 'expiry_date', 'image']

class ProductSearchForm(SearchForm):
    SORT_CHOICES = [
        ('name', 'Name (A-Z)'),
        ('-name', 'Name (Z-A)'),
        ('price', 'Price: low to high'),
        ('-price', 'Price: high to low'),
        ('-created_at', 'Newest first'),
        ('', '---')
    ]
    sort_by = forms.ChoiceField(choices=SORT_CHOICES, label='Sort by:', required=False)
from django import forms
from FarmersMarket.producers.models import Producer

class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter producer name'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter producer address'}),
            'country': forms.Select(attrs={'placeholder': 'Select country'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Producer description...'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Contact person'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'}),
            'website': forms.URLInput(attrs={'placeholder': 'Website'}),
            'image': forms.FileInput(),
        }

        labels = {
            'name': 'Producer Name:',
            'address': 'Producer Address:',
            'country': 'Country:',
            'description': 'Producer Description:',
            'contact': 'Contact Person:',
            'email': 'Email:',
            'phone': 'Phone Number:',
            'website': 'Website:',
        }

class ProducerCreateForm(ProducerForm):
    pass

class ProducerUpdateForm(ProducerForm):
    pass

class ProducerDeleteForm(ProducerForm):
    pass

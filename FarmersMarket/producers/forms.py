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

        help_texts = {
            'country': 'Select the country where the producer is located.',
            'contact': 'Enter the contact person for the producer.',
            'image': 'Upload an image of the producer.'
        }

        error_messages = {
            'name': {
                'required': 'Please enter the producer name.',
                'unique': 'Producer with this name already exists.'
            },
            'address': {'required': 'Please enter the producer address.'},
            'country': {'required': 'Please select a country.'},
            'contact': {'required': 'Please enter the contact person.'},
            'email': {'required': 'Please enter the email address.'},
            'phone': {'required': 'Please enter the phone number.'},
        }

class ProducerCreateForm(ProducerForm):
    pass

class ProducerUpdateForm(ProducerForm):
    pass

class ProducerDeleteForm(ProducerForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['name'].disabled = True
            self.fields['address'].disabled = True
            self.fields['country'].disabled = True

    class Meta(ProducerForm.Meta):
        exclude = ['description', 'contact', 'email', 'phone', 'website', 'image']

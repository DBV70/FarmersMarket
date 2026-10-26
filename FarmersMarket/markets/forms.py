from django import forms
from FarmersMarket.markets.models import MarketDay

class MarketForm(forms.ModelForm):
    class Meta:
        model = MarketDay
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'market_type': forms.Select(),
            'location': forms.TextInput(attrs={'placeholder': 'Enter market location'}),
            'description': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Market description...'}),
            'market_open': forms.TimeInput(attrs={'type': 'time', 'min': '08:00', 'max': '12:00'}, format='%H:%M'),
            'market_close': forms.TimeInput(attrs={'type': 'time', 'min': 'market_open', 'max': '19:00'}, format='%H:%M'),
            'producers': forms.SelectMultiple(),
        }

        labels = {
            'date': 'Date:',
            'market_type': 'Market Type:',
            'location': 'Location:',
            'market_open': 'Market Open:',
            'market_close': 'Market Close:',
            'producers': 'Producers:',
        }

        help_texts = {
            'date': 'Select the date of the market.',
            'market_type': 'Select the type of market.',
            'location': 'Enter the location of the market.',
            'market_open': 'Select the opening time of the market.',
            'market_close': 'Select the closing time of the market.',
            'producers': 'Select the producers associated with the market.',
        }

        error_messages = {
            'date': {'required': 'Please select a date.'},
            'market_type': {'required': 'Please select a market type.'},
            'location': {'required': 'Please enter the market location.'},
            'market_open': {'required': 'Please select the market opening time.'},
            'market_close': {'required': 'Please select the market closing time.'},
            'producers': {'required': 'Please select at least one producer.'},
        }

class MarketCreateForm(MarketForm):
    pass

class MarketUpdateForm(MarketForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['date'].disabled = True
            self.fields['market_type'].disabled = True

class MarketDeleteForm(MarketForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].disabled = True
        self.fields['market_type'].disabled = True
        self.fields['location'].disabled = True
        self.fields['description'].disabled = True

    class Meta(MarketForm.Meta):
        exclude = ['market_open', 'market_close', 'producers']

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
            'market_open': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
            'market_close': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
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

class MarketCreateForm(MarketForm):
    pass

class MarketUpdateForm(MarketForm):
    pass

class MarketDeleteForm(MarketForm):
    pass

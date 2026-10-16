from django import forms

class SearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search by name...'}))
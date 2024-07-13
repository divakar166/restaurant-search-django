from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search for a dish', max_length=255, required=False)
    location = forms.CharField(label='Location', max_length=255, required=False)
    cuisine = forms.CharField(label='Cuisine', max_length=255, required=False)

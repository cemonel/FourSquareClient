from django import forms

from .models import Searcher

class SearcherForm(forms.ModelForm):

    class Meta:
        model = Searcher
        fields = ('location', 'food',)
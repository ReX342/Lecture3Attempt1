# https://docs.djangoproject.com/en/3.2/ref/forms/api/
from django import forms

class EntryForm(forms.Form):
    title = forms.CharField(initial='class')
    content = forms.CharField()

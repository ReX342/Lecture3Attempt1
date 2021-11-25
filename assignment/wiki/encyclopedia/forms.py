# https://docs.djangoproject.com/en/3.2/ref/forms/api/
from django import forms

class EntryForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(label='Content', max_length=100, widget=forms.Textarea)
    affl = forms.BooleanField(required=False)

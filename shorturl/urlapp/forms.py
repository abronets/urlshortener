from django import forms
from urlapp.models import Url


class UrlForm(forms.ModelForm):
    long_url = forms.CharField(widget=forms.Textarea(
        attrs={
            'autofocus': True,
            'placeholder': 'Введіть ссилку',
            'class': 'form-control'
        }),
    )

    class Meta:
        model = Url
        fields = ('long_url',)
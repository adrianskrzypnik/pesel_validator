from django import forms

class PeselForm(forms.Form):
    pesel = forms.CharField(
        label='Numer PESEL',
        max_length=11,
        min_length=11,
        widget=forms.TextInput(attrs={
            'placeholder': 'Wprowadź 11-cyfrowy numer PESEL',
            'pattern': '\d{11}',
            'title': 'Wprowadź 11 cyfr'
        })
    )
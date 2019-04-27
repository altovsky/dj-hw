from django import forms
from django.conf import settings


class HomeForm(forms.Form):
    guessing_number = forms.IntegerField(label='Число')

    def clean_guessing_number(self):
        guessing_number = self.cleaned_data.get('guessing_number')
        if not (1 >= guessing_number <= settings.RANDOM_NUMBER_RANGE):
            raise forms.ValidationError(f"Число должно быть в диапазоне от 1 до {'settings.RANDOM_NUMBER_RANGE'}")
        return guessing_number

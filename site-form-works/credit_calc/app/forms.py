from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара")
    rate = forms.IntegerField(label="Процентная ставка")
    months_count = forms.IntegerField(label="Срок кредита в месяцах")

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if initial_fee == 0:
            raise forms.ValidationError('Стоимость товара не может быть нулевой')
        elif initial_fee < 0:
            raise forms.ValidationError('Стоимость товара не может быть отрицательной')
        return initial_fee

    def clean_rate(self):
        rate = self.cleaned_data.get('rate')
        if rate == 0:
            raise forms.ValidationError('Процентная ставка не может быть нулевой')
        elif rate < 0:
            raise forms.ValidationError('Процентная ставка не может быть отрицательной')
        return rate

    def clean_months_count(self):
        months_count = self.cleaned_data.get('months_count')
        if months_count == 0:
            raise forms.ValidationError('Срок кредита не может быть нулевым')
        elif months_count < 0:
            raise forms.ValidationError('Срок кредита не может быть отрицательным')
        return months_count

    def clean(self):
        # общая функция валидации
        return self.cleaned_data

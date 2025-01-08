from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='',
        widget=forms.NumberInput(
            attrs={
                'class': 'w-20 py-2 px-3 border-2 border-pink-500 rounded-lg focus:ring-2 focus:ring-pink-500 focus:border-pink-500 text-lg font-medium text-pink-500',
                'min': '1',
                'max': '20',
                'value': '1',
                'step': '1'
            }
        )
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
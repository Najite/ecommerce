from secrets import choice
from django import forms
from pkg_resources import require

PRODUCT_QUANTITY_FORM = [(i, str(i)) for i in range(1,11)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(coerce=int, 
                                      choices = PRODUCT_QUANTITY_FORM)
    
    override = forms.BooleanField(required=False,
                                           initial=False,
                                           widget=forms.HiddenInput)
    
    
    
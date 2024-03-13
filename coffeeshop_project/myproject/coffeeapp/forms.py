from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(label='search',max_length=50)


from. models import ShippingAddress1

PRODUCT_QUANTITY_CHOICES=[(i,str(i)) for i in range(1,21)]
class CartAddProductForm(forms.Form):
    quantity=forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)

class ShippingAddress1Form(forms.ModelForm):
    class Meta:
        model=ShippingAddress1
        fields=['building_name','street','landmark','city','state','zipcode']

from django import forms
from .models import Invoice,InvoiceItem
from crispy_forms.helper import FormHelper
from django.forms.models import inlineformset_factory




# class InvoiceForm(forms.ModelForm):
     
#     class Meta:
#         model = Invoice 
#         fields = ['invoice_number','customer_name']
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_class = 'CurrentProfile'

# class InvoiceItemForm(forms.ModelForm):

#     class Meta:
#         model = InvoiceItem 
#         fields = ['quantity']
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_class = 'CurrentProfile'

InvoiceFormSet = inlineformset_factory(Invoice,InvoiceItem,fields=('item','quantity',))

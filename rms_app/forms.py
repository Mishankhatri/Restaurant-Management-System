from django import forms
from .models import Invoice,InvoiceItem
from crispy_forms.helper import FormHelper
from django.forms.models import inlineformset_factory


InvoiceFormSet = inlineformset_factory(Invoice,InvoiceItem,fields=('item','quantity',))

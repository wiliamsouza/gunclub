"""
Invoice forms for gunclub
"""

from django import forms

from invoice.models import Invoice


class EditInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice

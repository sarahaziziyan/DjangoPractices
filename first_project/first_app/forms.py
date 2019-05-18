from django.forms import ModelForm, DateInput
from .models import *


class LibraryForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'


class MyDateInput(DateInput):
    input_type = 'date'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {'date_made': MyDateInput()}


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['nationalCode', 'firstName','lastName', 'email']





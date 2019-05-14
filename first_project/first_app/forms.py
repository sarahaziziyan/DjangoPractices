from django.forms import ModelForm
from .models import *

class LibraryForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'





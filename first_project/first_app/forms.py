from django.forms import ModelForm
from .models import *

class LibraryForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'





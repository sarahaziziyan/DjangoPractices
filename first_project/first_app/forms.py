from django.forms import ModelForm
from .models import *

class LibraryForm(ModelForm):
    class Meta:
        model=Library
        fields='__all__'




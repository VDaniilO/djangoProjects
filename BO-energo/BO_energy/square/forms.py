from django import forms
from .models import *

class Get_data_square(forms.Form):
    """
    Main forms for input data
    """
    value_a = forms.IntegerField()
    value_b = forms.IntegerField()
    value_c = forms.IntegerField()

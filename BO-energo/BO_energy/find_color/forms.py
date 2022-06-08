from django import forms
from .models import *

class Get_color(forms.ModelForm):
    """
    Class for get fields from database
    """
    class Meta:
        model = Number_info
        fields = ['number', 'color']
        widgets = {
            'number': forms.NumberInput(attrs={'max': 100})
        }

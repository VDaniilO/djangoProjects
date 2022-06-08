from django import forms
from .models import *

class Get_color(forms.ModelForm):
    class Meta:
        model = Number_info
        fields = ['number', 'color']

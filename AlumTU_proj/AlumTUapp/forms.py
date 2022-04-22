from django import forms
from .models import Alumni

class AlumniUpdateForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['image' , 'LinkedIn' ,'PhoneNumber']


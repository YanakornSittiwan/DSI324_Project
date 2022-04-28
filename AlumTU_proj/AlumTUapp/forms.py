from django import forms
from .models import Alumni,Achievement,Job
from django.forms import formset_factory

class AlumniUpdateForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['image' , 'LinkedIn','Line' ,'PhoneNumber','Address','Sub_District','District','Province','Postal_code']


class AchievementUpdateForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['Achievement_name' , 'Institute' , 'Date']

class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['Company_num' ,'Job_title','Department', 'Start_date','end_date']
















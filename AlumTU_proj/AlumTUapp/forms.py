from django import forms
from .models import Alumni,Achievement,Job

class AlumniUpdateForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['image' , 'LinkedIn','Line' ,'PhoneNumber','Province','District','Sub_District','Postal_code']


class AchievementUpdateForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['Achievement_name' , 'Institute' , 'Date']

class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['Job_title','Department' ]












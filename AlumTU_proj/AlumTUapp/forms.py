from django import forms
from .models import Alumni,Achievement,Job,Education
from django.forms import formset_factory

class AlumniUpdateForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['image', 'Name' , 'Surname' , 'LinkedIn','Line','Email' ,'PhoneNumber','Address','Sub_District','District','Province','Postal_code']

class DateInput(forms.DateInput):
    input_type = 'date'

class AchievementUpdateForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['Achievement_name' , 'Institute' , 'Date']
        widgets = {
            'Date': DateInput(),
        }

class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['Company' ,'Job_title','Department', 'Start_date','end_date','Consent']
        widgets = {
            'Start_date': DateInput(),
            'end_date': DateInput()
            
        }

class EducationUpdateForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'















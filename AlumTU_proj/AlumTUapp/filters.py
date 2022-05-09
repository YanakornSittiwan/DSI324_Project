import django_filters
from django_filters import DateFilter,CharFilter

from .models import *

class Jobfilter(django_filters.FilterSet):

    class Meta:
        model = Job
        # fields = ['Job_title','Company','Department',]
        fields = {
            'Job_title' : ['icontains'],
            'Company' : ['exact'],
            'Department' : ['exact'],
        }
    



class Educationfilter(django_filters.FilterSet):

    graduated_above = DateFilter(field_name="Graduated_date" , lookup_expr='gte')
    graduated_below = DateFilter(field_name="Graduated_date" , lookup_expr='lte')

    CHOICES = (
        ('Ascending_Educated_date','ปีที่เข้ารับการศึกษา น้อยไปมาก'),
        ('Ascending_Graduated_date','ปีที่จบการศึกษา น้อยไปมาก'),
        ('Decending_Educated_date','ปีที่เข้ารับการศึกษา มากไปน้อย'),
        ('Decending_Graduated_date','ปีที่จบการศึกษา มากไปน้อย'),
    )

    ordering = django_filters.ChoiceFilter(label="Order by",choices=CHOICES,method='filter_by_order')

    class Meta:
        model = Education
        # fields = ['Course','Educated_date','Graduated_date']
        fields = {
            'Course' : ['exact'],
        }
    
    def filter_by_order(self,queryset,name,value):
        if value == 'Ascending_Educated_date':
            expression = 'Educated_date'
        elif value == 'Ascending_Graduated_date':
            expression ='Graduated_date'
        elif value == 'Decending_Graduated_date':
            expression = '-Graduated_date'
        elif value == 'Decending_Educated_date':
            expression = '-Educated_date'
        # expression = 'Job_title' if value == 'Job_title' else 'Department'
        return queryset.order_by(expression)




import django_filters

from .models import *

class Jobfilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ['Company','Department',]

    

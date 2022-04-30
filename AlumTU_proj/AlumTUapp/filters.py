import django_filters

from .models import *

class Jobfilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ['Job_title','Department','Company']


# class Companyfilter(django_filters.FilterSet):
#     class Meta:
#         model = Company
#         fields = ['Sector','Industry_sector'] 

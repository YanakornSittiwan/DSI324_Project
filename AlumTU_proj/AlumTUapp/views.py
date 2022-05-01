from django.shortcuts import render, redirect
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Role,Alumni,Achievement,Company,Job,Course,Education
from .forms import AlumniUpdateForm,AchievementUpdateForm,JobUpdateForm,DateInput
from django.forms.models import modelformset_factory
from .forms import AchievementUpdateForm
from urllib import request
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.urls import reverse
from .filters import Jobfilter , Companyfilter
from django.forms.widgets import Select, Widget
from django import forms


# Create your views here.

def signuppage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            
            login(request,user)
            return redirect("/login")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    
def loginpage(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/profile')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def home(request):
    return render(request,'home.html')


class Alumnilist(ListView):
    model = Alumni
    template_name = 'alumni_list.html'



def alumni_list(request):
    alumni = Alumni.objects.all()
    return render(request,'alumni_list.html',{'alumni':alumni})



def connection(request):
    job = Job.objects.filter(Consent=True)
    
    myFilterjob = Jobfilter(request.GET,queryset=job)
    jobs = myFilterjob.qs

    context = {
        'job':jobs,
        'myFilterjob':myFilterjob,
    }
    return render(request, 'conection.html' , context)


def profile(request):
    alumni = Alumni.objects.all()
    achievement = Achievement.objects.all().order_by('-Date')
    education = Education.objects.all().order_by('-Graduated_date')
    course = Course.objects.all()
    company = Company.objects.all()
    job = Job.objects.all().order_by('-Start_date')
    return render(request,'profile.html',context = {'alumni':alumni , 'achievement':achievement ,'education':education,'course':course ,'company':company,'job':job })



def updatepro(request):
    achievement = Achievement.objects.filter(Alumni_id=request.user.alumni)
    AchievementFormSet = modelformset_factory(Achievement, form = AchievementUpdateForm , extra=0)

    job = Job.objects.filter(Alumni_id=request.user.alumni)
    JobFormset = modelformset_factory(Job, form = JobUpdateForm , extra=0)

    if request.method == 'POST':      
        a_form = AlumniUpdateForm(request.POST ,request.FILES, instance = request.user.alumni)
        ac_formset = AchievementFormSet(request.POST , queryset = achievement)
        j_formset = JobFormset(request.POST , queryset = job)
        if  all([a_form.is_valid ,ac_formset.is_valid , j_formset.is_valid]):
            a_form.save()
            ac_formset.save()
            j_formset.save()
            return redirect('/profile/')
    else:
        a_form = AlumniUpdateForm(instance = request.user.alumni)
        ac_formset = AchievementFormSet(queryset = achievement)
        j_formset = JobFormset(queryset =job )

    context = {
        'a_form':a_form ,
        'ac_form':ac_formset,
        'j_form':j_formset
    }

    return render(request,'up.html' , context=context)

class DateInput(forms.DateInput):
    input_type = 'date'


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['Company' ,'Job_title','Department','Start_date','end_date','Consent']
        widgets = {
            'Start_date' : DateInput(),
            'end_date': DateInput(),
        }

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['Achievement_name','Institute','Date']
        widgets = {
            'Date' : DateInput(),
        }


class AchievementCreateView(CreateView):
    form_class = AchievementForm
    model = Achievement
    template_name = 'Achievement_create.html'

    def form_valid(self, form):
        form.instance.Alumni_id = self.request.user.alumni
        return super().form_valid(form)

    success_url="/profile/up/"


class JobCreateView(CreateView):
    form_class = JobForm
    model = Job
    template_name = 'Job_create.html'
    
    def form_valid(self, form):
        form.instance.Alumni_id = self.request.user.alumni
        return super().form_valid(form)
    success_url="/profile/up/"

from django.db.models import Count


def AlumniChart(request):

    Sector_count=Job.objects.values('Company__Sector').annotate(Count('Company__Sector'))
    Industry_sector_count=Job.objects.values('Company__Industry_sector').annotate(Count('Company__Industry_sector'))
    Campus_count=Education.objects.values('Course__Campus').annotate(Count('Course__Campus'))
    Faculty_count=Education.objects.values('Course__Faculty').annotate(Count('Course__Faculty'))
    Course_title_count=Education.objects.values('Course__Course_title').annotate(Count('Course__Course_title'))
    context  = {
        'Sector_count':Sector_count,
        'Industry_sector_count':Industry_sector_count,
        'Campus_count':Campus_count,
        'Faculty_count':Faculty_count,
        'Course_title_count':Course_title_count,
    }
    return render(request, 'chart.html', context)


def terms(request):
    return render(request,'terms-conditions.html')













    







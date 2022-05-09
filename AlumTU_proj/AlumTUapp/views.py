from django.shortcuts import render, redirect
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Role,Alumni,Achievement,Company,Job,Course,Education,Personel
from .forms import AlumniUpdateForm,AchievementUpdateForm,JobUpdateForm,DateInput,EducationUpdateForm
from django.forms.models import modelformset_factory
from .forms import AchievementUpdateForm
from urllib import request
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.urls import reverse
from .filters import Jobfilter ,Educationfilter
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
            try:
                alum = Alumni.objects.get(User_id=user)
            except Alumni.DoesNotExist:
                alum = None
            try:
                perso = Personel.objects.get(User_id=user)
            except Personel.DoesNotExist:
                perso = None
            
            if alum != None:
                if user == alum.User_id:
                    login(request,user)
                    return redirect('/profile')
            else:
                if perso.personel_type == 'officer':
                    login(request,user)
                    return redirect('/alumlist')
                elif perso.personel_type == 'dean':
                    login(request,user)
                    return redirect('/dean/con')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def home(request):
    return render(request,'home.html')




def connection(request):
    job = Job.objects.filter(Consent=True)
    education = Education.objects.all()
    myFilterjob = Jobfilter(request.GET,queryset=job)
    jobs = myFilterjob.qs

    context = {
        'job':jobs,
        'myFilterjob':myFilterjob,
        'education' : education
    }
    return render(request, 'conection.html' , context)


def connection2(request):
    job = Job.objects.filter(Consent=True)
    education = Education.objects.all()
    myFilterjob = Jobfilter(request.GET,queryset=job)
    jobs = myFilterjob.qs

    context = {
        'job':jobs,
        'myFilterjob':myFilterjob,
        'education' : education
    }
    return render(request, 'conection2.html' , context)

def connection3(request):
    job = Job.objects.filter(Consent=True)
    education = Education.objects.all()
    myFilterjob = Jobfilter(request.GET,queryset=job)
    jobs = myFilterjob.qs

    context = {
        'job':jobs,
        'myFilterjob':myFilterjob,
        'education' : education
    }
    return render(request, 'conection3.html' , context)


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

    Department_count=Job.objects.values('Department').annotate(Count('Department'))
    Sector_count=Job.objects.values('Company__Sector').annotate(Count('Company__Sector'))
    Industry_sector_count=Job.objects.values('Company__Industry_sector').annotate(Count('Company__Industry_sector'))
    Campus_count=Education.objects.values('Course__Campus').annotate(Count('Course__Campus'))
    Faculty_count=Education.objects.values('Course__Faculty').annotate(Count('Course__Faculty'))
    Course_title_count=Education.objects.values('Course__Course_title').annotate(Count('Course__Course_title'))
    context  = {
        'Department_count':Department_count,
        'Sector_count':Sector_count,
        'Industry_sector_count':Industry_sector_count,
        'Campus_count':Campus_count,
        'Faculty_count':Faculty_count,
        'Course_title_count':Course_title_count,
    }
    return render(request, 'chart.html', context)


def terms(request):
    return render(request,'terms-conditions.html')


def AlumniChart2(request):

    Department_count=Job.objects.values('Department').annotate(Count('Department'))
    Sector_count=Job.objects.values('Company__Sector').annotate(Count('Company__Sector'))
    Industry_sector_count=Job.objects.values('Company__Industry_sector').annotate(Count('Company__Industry_sector'))
    Campus_count=Education.objects.values('Course__Campus').annotate(Count('Course__Campus'))
    Faculty_count=Education.objects.values('Course__Faculty').annotate(Count('Course__Faculty'))
    Course_title_count=Education.objects.values('Course__Course_title').annotate(Count('Course__Course_title'))
    context  = {
        'Department_count':Department_count,
        'Sector_count':Sector_count,
        'Industry_sector_count':Industry_sector_count,
        'Campus_count':Campus_count,
        'Faculty_count':Faculty_count,
        'Course_title_count':Course_title_count,
    }
    return render(request, 'chart2.html', context)


def terms(request):
    return render(request,'terms-conditions.html')


def alumlist(request):
    education = Education.objects.all()

    Filteredu = Educationfilter(request.GET,queryset=education)
    educations = Filteredu.qs
    context = {
        'education':educations,
        'Filteredu':Filteredu,
    }
    return render(request,'alumlist.html',context)


def update_education(request, pk):
    education = Education.objects.get(Education_id=pk)
    edu_form = EducationUpdateForm(instance=education)

    if request.method == 'POST':
        edu_form = EducationUpdateForm(request.POST, instance=education)
        if edu_form.is_valid():
            edu_form.save()
            return redirect('/alumlist/')
    else:
        edu_form = EducationUpdateForm(instance=education)

    context = {'edu_form':edu_form}    
    return render(request,'edu_update.html',context)

def alumni_info(request, pk, epk):
    alumni = Alumni.objects.get(Alumni_id=pk)
    education = Education.objects.get(Education_id=epk)
    job = Job.objects.filter(Alumni_id=pk)
    achievement= Achievement.objects.filter(Alumni_id=pk)

    context = {
        'alumni':alumni,
        'education':education,
        'job':job,
        'achievement':achievement
    }
    return render(request,'alumni_info.html',context)



        





















    







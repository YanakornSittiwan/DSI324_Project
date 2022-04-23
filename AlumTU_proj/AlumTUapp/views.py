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
from .forms import AlumniUpdateForm,AchievementUpdateForm,JobUpdateForm
from .forms import AchievementUpdateForm
from urllib import request
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView

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



def profile(request):
    alumni = Alumni.objects.all()
    achievement = Achievement.objects.all()
    education = Education.objects.all()
    course = Course.objects.all()
    company = Company.objects.all()
    job = Job.objects.all()
    return render(request,'profile.html',context = {'alumni':alumni , 'achievement':achievement ,'education':education,'course':course ,'company':company,'job':job })


def updatepro(request):
    achievement = Achievement.objects.get(Alumni_id=request.user.alumni)
    if request.method == 'POST':      
        a_form = AlumniUpdateForm(request.POST ,request.FILES, instance = request.user.alumni)
        ac_form = AchievementUpdateForm(request.POST , instance =achievement)
        if  a_form.is_valid and ac_form.is_valid:
            a_form.save()
            ac_form.save()
            return redirect('/profile/')
    else:
        a_form = AlumniUpdateForm(instance = request.user.alumni)
        ac_form = AchievementUpdateForm(instance =achievement)

    context = {
        'a_form':a_form ,
        'ac_form':ac_form
    }

    return render(request,'up.html' , context=context)


def newup(request):
    alup = AlumniUpdateForm
    acup = AchievementUpdateForm
    achievement = Achievement.objects.get(Alumni_id=request.user.alumni)
    a_form = AlumniUpdateForm(request.POST or None,instance = request.user.alumni)
    ac_form = AchievementUpdateForm(request.POST or None,instance = achievement)
    if request.method == 'POST':
        if  a_form.is_valid and ac_form.is_valid():
            a_form.save()
            ac_form.save()
            return redirect('/profile/')

    context = {
    'a_form':a_form ,
    'ac_form':ac_form,
    }

    return render(request,'up2.html' , context=context)




class AlumniList(ListView):
    model = Alumni
    template_name = 'al.html'




# class AuthorUpdateView(UpdateView):
#     model = Alumni
#     fields = ['LinkedIn']
#     template_name_suffix = '_update_form'

# class DesignerDetailView(DetailView):
#     model = Alumni
#     context_object_name = 'Alumni'
#     template_name = 'aldetail.html'
#     def get_object(self):
#         id_=self.kwargs.get('dpk')
#         return get_object_or_404(Designer,id=int(id_))


    
# def alumni_list(request):
#     alumni_list = Alumni.objects.all()
#     sys_user_list = Sys_User.object.all()
#     alumni_dict = {"designer":designer_list , "sys_user":sys_user_list}
#     return render(request,'.html',context=alumni_dict) ,request.FILES,instance = Alumni


# def edit_profile(request):  
#     a_form = AlumniUpdateForm()
#     if request.method == 'POST':
#             a_form = AlumniUpdateForm( request.POST)    
#             if a_form.is_valid():
#                 a_form.save()
#                 messages.success(request, f'updated')
#                 return redirect('profile')
#     else:
#         a_form = AlumniUpdateForm()
#     return render(request,'edit_profile.html',{'a_form':a_form})




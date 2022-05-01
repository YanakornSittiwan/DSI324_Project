"""AlumTU_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AlumTUapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView
# from AlumTUapp.views import AlumniList
from django.urls import path, include # New
from AlumTUapp.views import AchievementCreateView,JobCreateView

#from django.views.generic import TemplateView # New

urlpatterns = [
    path('',views.loginpage,name='login'),
    path('admin/', admin.site.urls),
    path('login/',views.loginpage,name='login'),
    path('signup/',views.signuppage),
    path('logout/', views.user_logout, name='logout'),
    path('home/',views.home),
    path('profile/',views.profile),
    path('profile/up/',views.updatepro),
    path('profile/up/arcreate/',AchievementCreateView.as_view()),
    path('profile/up/jobcreate/',JobCreateView.as_view()),
    path('con/',views.connection),
    path('chart/',views.AlumniChart),
    path('profile/up/terms/',views.terms),
    path('profile/up/jobcreate/terms/',views.terms),
    # path('arcup/<int:dpk>/',AchievementUpdateView.as_view()),




    #path('', TemplateView.as_view(template_name="login_page/index.html")), # New
    #path('accounts/', include('allauth.urls')), # New
]

if True:
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
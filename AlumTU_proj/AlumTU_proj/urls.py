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
    #Alumni's url
    path('',views.loginpage,name='login'),
    path('admin/', admin.site.urls),
    path('login/',views.loginpage,name='login'),
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

    #officer's url
    path('alumlist/',views.alumlist),
    path('update_education/<str:pk>/', views.update_education, name="update_education"),
    path('aluminfo/<str:pk>/<str:epk>/', views.alumni_info, name="aluminfo"),
    path('officer/con/',views.connection2),

    #deans's url
    path('dean/con/',views.connection3),
    path('dean/chart/',views.AlumniChart2),

    #API url
    path('api/alumni/',views.AlumniList.as_view()),
    path('api/alumni/<int:pk>',views.AlumniDetail.as_view()),

    path('api/personel/',views.PersonelList.as_view()),
    path('api/personel/<int:pk>',views.PersonelDetail.as_view()),

    path('api/company/',views.CompanylList.as_view()),
    path('api/company/<int:pk>',views.CompanyDetail.as_view()),

    path('api/achievement/',views.AchievementlList.as_view()),
    path('api/achievement/<int:pk>',views.AchievementDetail.as_view()),

    path('api/job/',views.JobList.as_view()),
    path('api/job/<int:pk>',views.JobDetail.as_view()),

    path('api/course/',views.CourseList.as_view()),
    path('api/course/<int:pk>',views.CourseDetail.as_view()),

    path('api/education/',views.EducationList.as_view()),
    path('api/education/<int:pk>',views.EducationDetail.as_view()),
    path('api-auth/', include('rest_framework.urls'))  # New

]

if True:
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
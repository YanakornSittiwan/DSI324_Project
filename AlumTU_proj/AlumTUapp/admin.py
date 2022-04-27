from django.contrib import admin
from . import models
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password
import pandas as pd
# Register your models here.
from django.urls import path
from .models import Role,Alumni,Achievement,Company,Job,Course,Education,User

admin.site.register(Role)
admin.site.register(Achievement)
admin.site.register(Company)
admin.site.register(Job)


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class UserAdmin(BaseUserAdmin):
    # list_display = ('username','first_name','last_name','password')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data[1:]:
                fields = x.split(",")

                #u = User(username=fields[0],first_name=fields[1], last_name=fields[2] , password=make_password(fields[3]))
                #u.save()
                created = User.objects.update_or_create(
                    username = fields[0],
                    first_name = fields[1],
                    last_name = fields[2],
                    password = make_password(fields[3])
                    )


            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class AlumniAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data[1:]:
                fields = x.split(",")
                created = Alumni.objects.update_or_create(
                    Alumni_id = fields[0],
                    User_id = User.objects.get(username=fields[1]),
                    Name=fields[2],
                    Surname=fields[3],
                    Province=fields[4],
                    District=fields[5],
                    Sub_District=fields[6],
                    Postal_code=fields[7],
                    Address = fields[8],
                    PhoneNumber=fields[9]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Alumni, AlumniAdmin)


class CourseAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data[1:]:
                fields = x.split(",")
                created = Course.objects.update_or_create(
                    Course_id = fields[0],
                    Course_title = fields[1],
                    Faculty=fields[2],
                    Campus=fields[3],
                    Credits=fields[4],
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Course, CourseAdmin)

class EducationAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data[1:]:
                fields = x.split(",")
                created = Education.objects.update_or_create(
                    Education_id = fields[0],
                    Alumni_id = Alumni.objects.get(Alumni_id=fields[1]),
                    Course_id= Course.objects.get(Course_id=fields[2]),
                    Degree=fields[3],
                    Gpa=fields[4],
                    Educated_date = fields[5],
                    Graduated_date =fields[6] 
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Education, EducationAdmin)
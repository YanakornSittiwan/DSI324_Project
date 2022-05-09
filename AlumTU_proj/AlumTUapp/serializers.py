from rest_framework import serializers
from .models import Alumni,Achievement,Company,Job,Course,Education,User,Personel

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = ('Alumni_id','User_id','Name' , 'Surname' , 'LinkedIn','Line','Email' ,'PhoneNumber','Address','Sub_District','District','Province','Postal_code','image')


class PersonelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personel
        fields = ('Personel_id','personel_type','User_id','Name' , 'Surname','Email')

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('Achievement_id','Alumni_id','Achievement_name' , 'Institute' , 'Date')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('Company_num','Name','Industry_sector','Sector','Sub_District','District','Province','Postal_code')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (',Job_id','Alumni_id','Company' ,'Job_title','Department', 'Start_date','end_date','Consent')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('Course_id','Course_title','Faculty','Campus','Credits')

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('Education_id','Alumni_id','Course','Degree','Gpa','Educated_date','Graduated_date')
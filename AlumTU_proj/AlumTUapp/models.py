from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    Role = models.CharField(max_length=50 , primary_key=True)
    Authority = models.CharField(max_length=256)

class Alumni(models.Model):
    Alumni_id = models.IntegerField(max_length=10 , primary_key=True)
    User_id = models.OneToOneField(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=50 , null=True)
    Surname = models.CharField(max_length=50 , null=True)
    image = models.ImageField(default = 'default.jpg',upload_to='profile_pic')
    LinkedIn = models.CharField(max_length=256)
    Province = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    Sub_District = models.CharField(max_length=50)
    Postal_code = models.IntegerField(max_length=5)
    PhoneNumber = models.IntegerField(max_length=10, null=True)
    def __str__(self):
        return ("Alumni id:%s mobile:%s" %(self.User_id,self.PhoneNumber))




class Achievement(models.Model):
    Achievement_id = models.IntegerField(max_length=10 , primary_key=True)
    Alumni_id = models.ForeignKey(Alumni, on_delete = models.CASCADE)
    Achievement_name = models.CharField(max_length=256)
    Institute = models.CharField(max_length=50)
    Date = models.DateField()
    
class Company(models.Model):
    Company_num = models.IntegerField(max_length=13 , primary_key=True)
    Name = models.CharField(max_length=50)
    Industry_sector = models.CharField(max_length=50)
    Sector = models.CharField(max_length=50)
    Province = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    Sub_District = models.CharField(max_length=50)
    Postal_code = models.IntegerField(max_length=5)

class Job(models.Model):
   Job_id = models.IntegerField(max_length=10 , primary_key=True)
   Alumni_id = models.ForeignKey(Alumni, on_delete = models.CASCADE)
   Company_num = models.ForeignKey(Company, on_delete = models.CASCADE)
   Department = models.CharField(max_length=50)
   Job_title = models.CharField(max_length=50)
   Start_date = models.DateField()
   end_date = models.DateField()

class Course(models.Model):
    Course_id = models.IntegerField(max_length=10 , primary_key=True)
    Course_title = models.CharField(max_length=50)
    Faculty = models.CharField(max_length=50)
    Campus = models.CharField(max_length=10)
    Credits = models.FloatField(max_length=4)

class Education(models.Model):
    Education_id = models.IntegerField(max_length=10 , primary_key=True)
    Alumni_id = models.ForeignKey(Alumni, on_delete = models.CASCADE)
    Course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    Degree = models.CharField(max_length=50)
    Gpa = models.FloatField(max_length=4)
    Educated_date = models.DateField()
    Graduated_date = models.DateField()
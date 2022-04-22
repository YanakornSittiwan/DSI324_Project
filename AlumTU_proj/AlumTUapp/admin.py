from django.contrib import admin
from . import models
# Register your models here.

from .models import Role,Alumni,Achievement,Company,Job,Course,Education

admin.site.register(Role)
admin.site.register(Alumni)
#admin.site.register(Sys_User)
admin.site.register(Achievement)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Course)
admin.site.register(Education)

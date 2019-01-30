# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: admin.py
# @Last modified by:   mlhale
# @Last modified time: 2019-01-30T13:59:14-08:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale



from django.contrib import admin

#if ENVIRONMENT == 'PROD':
#	from api.models import *
#else:
from api.models import Capability, Role, HospitalObject

# Register your models here.
admin.site.register(Capability)
admin.site.register(HospitalObject)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Role, RoleAdmin)

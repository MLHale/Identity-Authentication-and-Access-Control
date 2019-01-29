# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: admin.py
# @Last modified by:   mlhale
# @Last modified time: 2019-01-29T13:52:09-08:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale



from django.contrib import admin

#if ENVIRONMENT == 'PROD':
#	from api.models import *
#else:
from api.models import Item

# Register your models here.
admin.site.register(Item)

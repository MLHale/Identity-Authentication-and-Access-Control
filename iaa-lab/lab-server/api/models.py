# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: models.py
# @Last modified by:   mlhale
# @Last modified time: 2019-01-29T13:55:41-08:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale



from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.validators import *


class Item(models.Model):
	partname = models.CharField(max_length=100, blank=False)
	owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='items', blank=False)
	description = models.TextField(max_length=1000, blank=False)
	
	def __str__(self):
		return str(self.partname)

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('id', 'partname', 'owner', 'description')
		
class UserSerializer(serializers.ModelSerializer):
	lastname = serializers.CharField(source='last_name')
	firstname = serializers.CharField(source='first_name')
	issuperuser = serializers.CharField(source='is_superuser')
	class Meta:
		resource_name = 'users'
		model = User
		fields = ('id', 'username', 'lastname', 'firstname', 'email', 'issuperuser')

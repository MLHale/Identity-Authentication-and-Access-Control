# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: models.py
# @Last modified by:   mlhale
# @Last modified time: 2019-01-30T14:00:59-08:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale



from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.validators import *

class  HospitalObject(models.Model):
	name = models.CharField(max_length=100, blank=False)
	description = models.TextField(max_length=1000, blank=True)
	
	def __str__(self):
		return str(self.name)

class HospitalObjectSerializer(serializers.ModelSerializer):
	class Meta:
		model =  HospitalObject
		fields = ('id','name' 'description', 'roles')

class Capability(models.Model):
	name = models.CharField(max_length=100, blank=False)
	description = models.TextField(max_length=1000, blank=True)
	
	def __str__(self):
		return str(self.name)
		
	class Meta:
		verbose_name_plural = 'Capabilities'

class CapabilitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Capability
		fields = ('id','name', 'description', 'roles')

class Role(models.Model):
	name = models.CharField(max_length=100, unique=True, blank=False)
	description = models.TextField(max_length=1000, blank=True)
	users = models.ManyToManyField(User, related_name='roles', blank=True)
	capabilities = models.ManyToManyField(Capability, related_name="roles", blank=True)
	hospitalobjects = models.ManyToManyField(HospitalObject, related_name="roles", blank=True)
	
	def __str__(self):
		return str(self.name)

class RoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Role
		fields = ('id', 'name', 'description', 'users', 'capabilities')
		
class UserSerializer(serializers.ModelSerializer):
	lastname = serializers.CharField(source='last_name')
	firstname = serializers.CharField(source='first_name')
	issuperuser = serializers.CharField(source='is_superuser')
	class Meta:
		resource_name = 'users'
		model = User
		fields = ('id', 'username', 'lastname', 'firstname', 'email', 'issuperuser', 'roles')

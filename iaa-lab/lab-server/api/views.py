# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: controllers.py
# @Last modified by:   mlhale
# @Last modified time: 2019-01-29T13:59:35-08:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale


# Handy Django Functions
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
import datetime, pytz

# Models and serializers
from django.contrib.auth.models import User
import api.models as api

# REST API Libraries
from rest_framework import viewsets, parsers, renderers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import list_route
from rest_framework.authentication import *

from api.pagination import *

from django.core import serializers
from django.core.exceptions import ValidationError

def staff_or_401(request):
	if not request.user.is_staff:
		return Response({'success': False},status=status.HTTP_401_UNAUTHORIZED)

def super_user_or_401(request):
	if not request.user.is_superuser:
		return Response({'success': False},status=status.HTTP_401_UNAUTHORIZED)

def admin_or_401(request):
	if not (request.user.is_staff or request.user.is_superuser):
		return Response({'success': False},status=status.HTTP_401_UNAUTHORIZED)

class ItemViewSet(viewsets.ModelViewSet):
	"""
	Endpoint to view the items
	"""
	resource_name = 'items'
	serializer_class = api.ItemSerializer
	queryset = api.Item.objects.all()
	permission_classes = (AllowAny,)
	filter_fileds = ('id', 'partname', 'owner', 'checkedoutto')

	def create(self, request):
		admin_or_401(request)

		serializer = api.ItemSerializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		serializer.save()

		return Response(serializer.data)

	def update(self, request, pk=None):
		admin_or_401(request)

		serializer = api.ItemSerializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		serializer.save()

		return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
	"""
	Endpoint that allows user data to be viewed.
	"""
	resource_name = 'users'
	serializer_class = api.UserSerializer
	queryset = User.objects.all()
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		user = self.request.user
		if user.is_superuser:
			return User.objects.all()
		return User.objects.filter(username=user.username)

class Register(APIView):
	permission_classes = (AllowAny,)

	def post(self, request, *args, **kwargs):
		# Login
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		if username is not None and password is not None and email is not None:
			if User.objects.filter(username=username).exists():
				return Response({'username': 'Username is taken.', 'status': 'error'})
			elif User.objects.filter(email=email).exists():
				return Response({'email': 'Email is taken.', 'status': 'error'})
			# especially before you pass them in here
			newuser = User.objects.create_user(email=email, username=username, password=password)

			newprofile = api.Profile(user=newuser)

			newprofile.save()
			# Send email msg
			# send_templated_mail(
			#     template_name='welcome',
			#     from_email='from@example.com',
			#     recipient_list=[email],
			#     context={
			#         'username':username,
			#         'email':email,
			#     },
			#     # Optional:
			#     # cc=['cc@example.com'],
			#     # bcc=['bcc@example.com'],
			# )
			return Response({'status': 'success', 'userid': newuser.id, 'profile': newprofile.id})
		else:
			return Response({'status': 'error'})


class Session(APIView):
	"""
	Returns a JSON structure: {'isauthenticated':<T|F>,'userid': <int:None>,'username': <string|None>,'profileid': <int|None>}
	"""
	permission_classes = (AllowAny,)
	def form_response(self, isauthenticated, userid, username, profileid, error=""):
		data = {
			'isauthenticated': 	isauthenticated,
			'userid': 			userid,
			'username': 		username,
			'profileid':		profileid,
		}
		if error:
			data['message'] = error

		return Response(data)

	def get(self, request, *args, **kwargs):
		# Get the current user
		user = request.user
		if user.is_authenticated():
			profile = get_object_or_404(api.Profile,user__username=user.username)
			return self.form_response(True, user.id, user.username, profile.id)
		return self.form_response(False, None, None, None)

	def post(self, request, *args, **kwargs):
		print(request.data)
		# Login
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				profile = get_object_or_404(api.Profile,user__username=user.username)
				return self.form_response(True, user.id, user.username, profile.id)
			return self.form_response(False, None, None, None, "Account is suspended")
		return self.form_response(False, None, None, None, "Invalid username or password")

	def delete(self, request, *args, **kwargs):
		# Logout
		logout(request)
		return Response(status=status.HTTP_204_NO_CONTENT)

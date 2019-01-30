# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: urls.py
# @Last modified by:   mlhale
# @Last modified time: 2019-01-30T14:00:26-08:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale



from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers

from api import views
from django.views.decorators.csrf import csrf_exempt

#REST API routes
router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'users', views.UserViewSet)
# router.register(r'roles', views.RoleViewSet)
router.register(r'capabilties', views.CapabilityViewSet)
router.register(r'hospitalobjects', views. HospitalObjectViewSet)

urlpatterns = [
    url(r'^session', csrf_exempt(views.Session.as_view())),
    url(r'^register', csrf_exempt(views.Register.as_view())),
    url(r'^', include(router.urls)),
]

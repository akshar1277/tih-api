
from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serializers import ServicesSerializer,CoursesSerializer,ActivitiesSerializer,StartupsSerializer
from .models import Services ,Courses,Startups,Activities

class ServicesViewSet(viewsets.ModelViewSet):
    queryset=Services.objects.all().order_by('-id')
    serializer_class=ServicesSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset=Courses.objects.all().order_by('-id')
    serializer_class=CoursesSerializer

class StartupsViewSet(viewsets.ModelViewSet):
    queryset=Startups.objects.all().order_by('-id')
    serializer_class=StartupsSerializer

class ActivitiesViewSet(viewsets.ModelViewSet):
    queryset=Activities.objects.all().order_by('-id')
    serializer_class=ActivitiesSerializer

from rest_framework import serializers
from .models import Services ,Courses,Startups,Activities



class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Services
        fields=('id','title','image','desc')

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=('id','title','image','desc','price')

class StartupsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Startups
        fields=('id','title','image','desc')

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Activities
        fields=('id','title','desc')

from django.urls import path,include
from rest_framework import routers, urlpatterns
from .views import ServicesViewSet,CoursesViewSet,StartupsViewSet,ActivitiesViewSet


router=routers.DefaultRouter()
router.register(r'Services',ServicesViewSet)
router.register(r'Courses',CoursesViewSet)
router.register(r'Startups',StartupsViewSet)
router.register(r'Activities',ActivitiesViewSet)



urlpatterns = [
    path('',include(router.urls)),
]



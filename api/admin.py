from django.contrib import admin
from .models import Services ,Courses,Startups,Activities

class ServicesAdmin(admin.ModelAdmin):
    list_display=['title','image','desc']

class CoursesAdmin(admin.ModelAdmin):
    list_display=['title','image','desc','price']

class StartupsAdmin(admin.ModelAdmin):
    list_display=['title','image','desc']

class ActivitiesAdmin(admin.ModelAdmin):
    list_display=['title','desc']


# Register your models here.
admin.site.register(Services,ServicesAdmin)
admin.site.register(Courses,CoursesAdmin)
admin.site.register(Startups,StartupsAdmin)
admin.site.register(Activities,ActivitiesAdmin)

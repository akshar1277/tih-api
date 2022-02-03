from django.db import models
from gdstorage.storage import GoogleDriveStorage
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission
gd_storage = GoogleDriveStorage()


class Services(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Services/images", storage=gd_storage)
    desc=models.TextField(max_length=500)
    def __str__(self):
        return self.title


class Courses(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Courses/images", storage=gd_storage)
    desc=models.TextField(max_length=500)
    price=models.CharField(max_length=200)
    def __str__(self):
        return self.title
    


class Startups(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="Startups/images", storage=gd_storage)
    desc=models.TextField(max_length=500)
    def __str__(self):
        return self.title
    


class Activities(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField(max_length=500)
    def __str__(self):
        return self.title
    

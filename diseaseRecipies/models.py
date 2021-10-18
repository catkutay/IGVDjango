# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import django
from django.db import models



class Disease(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description=models.CharField(max_length=45,null=True)

    class Meta:
        db_table = 'disease'
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name

class Recipies(models.Model):
    id = models.AutoField(primary_key=True)
    #user = models.ForeignKey(User,on_delete= models.CASCADE,null=True)
    name = models.CharField(max_length=45,default="")
    audio = models.FileField(upload_to="audios/", default="")
    disease = models.ForeignKey(Disease,on_delete= models.CASCADE,null=True)
    image1 = models.ImageField(upload_to="images/", default="")
    description1 = models.TextField(max_length=400, default="")
    image2 = models.ImageField(upload_to="images/", default="")
    description2 = models.TextField(max_length=400, default="")
    image3 = models.ImageField(upload_to="images/", default="")
    description3 = models.TextField(max_length=400, default="")
    image4 = models.ImageField(upload_to="images/", default="")
    description4 = models.TextField(max_length=400, default="")

    class Meta:
        db_table = 'recipies'

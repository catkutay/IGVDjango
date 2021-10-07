# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    class Meta:
        db_table = 'user'

class Recipies(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete= models.CASCADE,null=True)
    disease = models.ForeignKey(Disease,on_delete= models.CASCADE,null=True)
    description = models.CharField(max_length=45)
    image1=models.ImageField(upload_to="images/",null=True)
    image2 = models.ImageField(upload_to="images/",null=True)
    image3 = models.ImageField(upload_to="images/",null=True)
    image4 = models.ImageField(upload_to="images/",null=True)

    class Meta:
        db_table = 'recipies'

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30, null=True)
    type_of_user = models.CharField(max_length=2, null=True)
    phonenumber = models.CharField(max_length=20, null=True)
    level = models.IntegerField(null=True)
    location = models.CharField(max_length=50)
    nearest_town = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    availability = models.CharField(max_length=50)



class session_levels(models.Model):
	  session_id = models.CharField(max_length=25,primary_key=True)
	  phonenumber= models.CharField(max_length=25,null=True)
	  level = models.IntegerField(null=True)

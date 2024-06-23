from django.db import models

# Create your models here.
class Contact_db(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,blank=True,null=True)
    Phone=models.IntegerField(null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=150,null=True,blank=True)
class Register_db(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Confirm_password=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,blank=True,null=True)
class CartDb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    ProductName=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Totalprice=models.IntegerField(null=True,blank=True)
class CheckoutDb(models.Model):
    Name=models.CharField(max_length=100, blank=True, null=True)
    Email = models.EmailField(max_length=100, blank=True, null=True)
    Address= models.EmailField(max_length=100, blank=True, null=True)
    Phone=models.IntegerField(null=True,blank=True)
    Totalprice = models.IntegerField(null=True, blank=True)

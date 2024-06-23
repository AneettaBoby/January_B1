from django.db import models

# Create your models here.
class ecommerce_db(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Desicription=models.CharField(max_length=100,null=True,blank=True)
    C_image = models.ImageField(upload_to="C_image", null=True, blank=True)

class product_db(models.Model):
    Category=models.CharField(max_length=200,null=True,blank=True)
    P_Name = models.CharField(max_length=100, null=True, blank=True)
    P_price=models.IntegerField(null=True, blank=True)
    Desicription = models.CharField(max_length=100, null=True, blank=True)
    P_image = models.ImageField(upload_to="P_image", null=True, blank=True)
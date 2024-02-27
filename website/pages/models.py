from sre_constants import CATEGORY
from typing import Any
from django.db import models

class companyinformation(models.Model):
   name =models.CharField(max_length=100)
   description =models.TextField()
  
   def __str__(self) -> str:
        return self.name
   
class Category(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self) -> str:
        return self.name

class product(models.Model):
   title =models.CharField(max_length=120)
   description =models.TextField(blank=True,null=True)
   category = models.ForeignKey(Category, on_delete= models.CASCADE) 
   image = models.ImageField(null = True)
   price =models.DecimalField(decimal_places=2,max_digits=1000)
   date =models.DateField(auto_now_add=True, null = True)

   def __str__(self) -> str:
        return self.title

class aboutcompany(models.Model):
   about_title =models.CharField(max_length=120)
   description =models.TextField(blank=True,null=True)
   Our_Vision = models.CharField(max_length=10000,null=True)
   Our_Goal = models.TextField(null=True)
   Our_Mission = models.CharField( max_length=50000,null=True)
    

   def __str__(self) -> str:
        return self.about_title
   
class place(models.Model):
   location_address =models.CharField(max_length=120)
   locaton_description =models.TextField(blank=True,null=True) 
   image = models.ImageField(null = True)

   def __str__(self) -> str:
        return self.location_address
  
class for_Contact(models.Model):
    To = models.CharField( max_length=50)
    email = models.CharField(max_length=50)
    Number = models.CharField( max_length=50)

    def __str__(self) -> str:
        return self.To


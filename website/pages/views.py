from django.http import HttpResponse
from django.shortcuts import render
from .models import*
# Create your views here.
#def home_view(*args,**kwargs):
 #return HttpResponse("<h1>hello world its working just trying out different methods</h1>")

def home(requests):
   info =companyinformation.objects.all().first()
   products =product.objects.all()

   data ={
    'info':info,
    'products':products

  }
   return render (requests, 'home.html',data)
  

def about(requests):
   about_title=aboutcompany.objects.all().first()
   description =aboutcompany.objects.all().first()
   #for_Contact=for_Contact.objects.all().first()

   data ={
      'about':about_title,
      'description':description,
      #'cont':for_Contact
   }

   return render (requests,'about.html',data)

def contact(requests):
   places = place.objects.all()
   location_address=place.objects.all().first()
   #for_Contact=for_Contact.objects.all().first()

   data={
      'places':places,
     'location_address':location_address,
     #'contact':for_Contact
  }
   return render(requests,'contact.html',data)

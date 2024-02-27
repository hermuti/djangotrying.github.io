from django.contrib import admin

# Register your models here.
from .models import product
from .models import Category
from .models import companyinformation
from .models import *

admin.site.register(product)
admin.site.register(Category)
admin.site.register(companyinformation)
admin.site.register(aboutcompany)
admin.site.register(place)
admin.site.register(for_Contact)
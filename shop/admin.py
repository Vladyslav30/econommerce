from django.contrib import admin
from .models import Category, Product
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)

#after all this, in terminal command line: python manage.py makemigrations

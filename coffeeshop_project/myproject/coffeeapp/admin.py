from django.contrib import admin
from .models import Coffee

class Coffeeadmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')
admin.site.register(Coffee,Coffeeadmin)






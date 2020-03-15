from django.contrib import admin
from .models import List, Items, Customer

#Create Admin templates for the models
class ItemAdmin(admin.ModelAdmin):
    list_display = ('idnumber', 'name', 'price', 'rating')

# Register your models here. helps manage models
admin.site.register(List)
admin.site.register(Items, ItemAdmin)
admin.site.register(Customer)
from django.contrib import admin
from . models import *
# Register your models here.

class VarietyAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'slug', 'image', 'created', 'updated')
    list_display_links =('id', 'name', 'slug')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Variety, VarietyAdmin)



class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'variety', 'meal', 'image', 'display', 'spicy', 'slug', 'time', 'price', 'discount', 'min_order', 'max_order', 'breakfast', 'lunch', 'dinner', 'updated')
    list_diaplay_links = ('id', 'variety', 'meal', 'slug')
    list_editable = ['display', 'discount']
    prepopulated_fields = {'slug':('meal',)}


admin.site.register(Meal, MealAdmin)




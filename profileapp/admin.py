from django.contrib import admin
from . models import *
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'subject', 'message', 'created', 'status', 'closed')
    list_display_links = ('id', 'name', 'phone')


admin.site.register(Contact, ContactAdmin)



class ProfileAdmin(admin.ModelAdmin):
    list_display = ['cart_code', 'user', 'first_name', 'last_name', 'email', 'phone', 'address', 'state', 'image']
    list_display_links = ['cart_code', 'user', 'first_name', 'last_name']

admin.site.register(Profile, ProfileAdmin)


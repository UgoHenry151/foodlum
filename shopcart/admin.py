from django.contrib import admin
from . models import *
# Register your models here.


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['id','user','meal','quantity','how_spicy','order_no','items_paid']
    list_display_links = ['id','user','meal']
    readonly_fields = ['id','user','meal','quantity','how_spicy','order_no','items_paid']

admin.site.register(ShopCart, ShopCartAdmin)


class PaidOrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','total','cart_no','payment_code','paid_item','first_name','last_name']
    list_display_links = ['id','user','cart_no','paid_item']
    readonly_fields = ['id','user','total','cart_no','payment_code','paid_item','first_name','last_name']

admin.site.register(PaidOrder, PaidOrderAdmin)


class ShippingAdmin(admin.ModelAdmin):
    list_display = ['id','user','meal','shipping_no','paid_cart','fname','lname','address','phone','state','status','admin_remark']
    list_display_links = ['id','user','meal']
    readonly_fields = ['id','user','meal','shipping_no','paid_cart','fname','lname','address','phone','state']

admin.site.register(Shipping, ShippingAdmin)
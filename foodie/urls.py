from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name = 'index'),
    path('meals', views.meals, name = 'meals'),
    path('searched', views.searched, name = 'searched'),
    path('mealdetail/<str:id>/<slug:slug>', views.mealdetail, name = 'mealdetail'),
    path('variety/<str:id>/<slug:slug>', views.variety, name = 'variety'),
    path('signin', views.signin, name = 'signin'),
    path('signout', views.signout, name = 'signout'),
    path('signup', views.signup, name = 'signup'),
    path('profile', views.profile, name = 'profile'),
    path('contact', views.contact, name = 'contact'),
    path('profileupdate', views.profileupdate, name = 'profileupdate'),
    path('passwordupdate', views.passwordupdate, name = 'passwordupdate'),   
    path('cart', views.cart, name = 'cart'), 
    path('remove_item', views.remove_item, name = 'remove_item'), 
    path('addtocart', views.addtocart, name = 'addtocart'),   
    path('checkout', views.checkout, name = 'checkout'),
    path('placeorder', views.placeorder, name = 'placeorder'),
    path('paidorder', views.paid_order, name = 'paidorder'),
]
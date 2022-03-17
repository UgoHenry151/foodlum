from re import sub
from sys import api_version
import uuid
import requests
import json

from email.policy import default
from json import load
from multiprocessing import context
from weakref import ref
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
from .models import *
from .forms import *
from profileapp.models import *
from shopcart.models import *


def index(request):
    breakfast = Meal.objects.filter(breakfast=True, display=True).order_by('-id')[:4]
    lunch = Meal.objects.filter(lunch=True, display=True).order_by('id')[:4]
    dinner = Meal.objects.filter(dinner=True, display=True).order_by('-id')[:4]
    variet = Variety.objects.all()

    context = {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'vee': variet
    }
    return render(request,'index.html', context)


def meals(request):
    # if 'itemsearch' in request.GET:
    #     searched = request.GET['itemsearch']
    #     meals = Meal.objects.filter(Q(Q(meal__icontains=searched)|Q(time__icontains=searched)))
    # else:
    meals = Meal.objects.all()
    # variet = Variety.objects.all()

    context = {
        'meals':meals,
        # 'vee':variet
    }
    return render(request,'meals.html', context)



def searched(request):
    if request.method == 'POST':
        searched = request.POST['itemsearch']
        searched_item = Q(Q(meal__icontains=searched)|Q(time__icontains=searched))
        searched_meals = Meal.objects.filter(searched_item)
    else:
        meals = Meal.objects.all()

    context = {
        'searched_meals':searched_meals
    }

    return render(request, 'searched.html', context)



def mealdetail(request, id, slug):
    mealdetail = Meal.objects.get(pk=id) 
    # variet = Variety.objects.all()

    context = {
        'mealdetail':mealdetail,
        # 'vee': variet
    }
    return render(request, 'mealdetail.html', context)


def variety(request, id, slug):
    variety = Meal.objects.filter(variety_id=id)
    single = Variety.objects.get(pk=id)
    # variet = Variety.objects.all()

    context = {
        'variety': variety, 
        'single': single,
        # 'vee': variet
    }
    return render(request, 'variety.html', context)


def contact(request):
    cform = ContactForm()
    if request.method == 'POST':
        cform = ContactForm(request.POST)
        if cform.is_valid():
            cform.save()
            messages.success(request, 'Thank you for contacting us! Our customer care agent would reach you soon.')
        return redirect('index')

    context = {
        'cform': cform
    }
    return render(request, 'index.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome {user.first_name}, its good to have you here!')
            return redirect('index')
        else:
            messages.info(request, ' Incorrect Username/Password, kindly check your details and try again, thank you.')
            return redirect('signin')  

    return render(request, 'login.html')


def signout(request):
    logout(request)
    messages.success(request, 'you have now signed out of your account.')
    return redirect('signin')


def signup(request):
    form = SignupForm() #instantiate the SignupForm for a GET request
    if request.method == 'POST': #check if a post method for persisting data to the DB
        phone = request.POST['phone']
        image = request.POST['image']
        form = SignupForm(request.POST) #instantiate the SignupForm for a POST request
        if form.is_valid():  #ensures security checks here
            user = form.save() #save data if data is valid
            profile = Profile(user = user)
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            profile.phone = phone
            profile.image = image
            profile.save()
            login(request, user)
            messages.success(request, 'Signup Successful!')
            return redirect('index') #send user to any page you desire in this case homepage
        else:
            messages.error(request, form.errors)

    context = {
        'form': form
    }
    return render(request,'signup.html', context)



@login_required(login_url='signin')
def profile(request):
    profile = Profile.objects.get(user__username= request.user.username)
    # variet = Variety.objects.all()

    context={
        'profile':profile,
        # 'vee': variet,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='signin')
def profileupdate(request):
    load_profile = Profile.objects.get(user__username= request.user.username)
    form = ProfileForm(instance= request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance= request.user.profile)
        if form.is_valid():
            figure = form.save()
            messages.success(request, f'Dear {figure.first_name} your profile update is successful!')
            return redirect('profile')
        else:
            messages.error(request, f'Dear {figure.first_name} kindly follow the following instructions {form.errors}, thank you.')
            return redirect('profile')

    context = {
        'load_profile':load_profile,
        'form':form,
    }
    return render(request, 'profileupdate.html', context)


@login_required(login_url='signin')
def passwordupdate(request):
    load_profile = Profile.objects.get(user__username= request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, f'Dear {user.first_name} your password update is successful!')
            return redirect(profile)
        else:
            messages.error(request, f'Dear {user.first_name} kindly follow the following instructions {form.errors}, thank you.')
            return redirect('passwordupdate')

    context = {
        'load_profile':load_profile,
        'form':form,
    }
    return render(request, 'passwordupdate.html', context)


@login_required(login_url='signin')
def addtocart(request):
    # cart_code = str(uuid.uuid4()) 
    cartno = Profile.objects.get(user__username = request.user.username)
    cart_code = cartno.cart_code 
    if request.method == 'POST':
        addquantity = int(request.POST['quantity'])
        addspice = request.POST['how_spicy']
        addid = request.POST['mealdetailid']
        mealid = Meal.objects.get(pk=addid)
        # addspicy = request.POST.get('spicy', None) #None represents whatever value is selected by the user

        cart = ShopCart.objects.filter(user__username = request.user.username, items_paid = False)
        if cart:
           # more = ShopCart.objects.filter(meal_id = mealid.id, user__username = request.user.username).first() #incrmenting method
            more = ShopCart.objects.filter(meal_id = mealid.id, quantity=addquantity, how_spicy=addspice, user__username = request.user.username).first()
            if more:
                more.quantity = addquantity
                more.how_spicy = addspice
                more.save()
                messages.success(request, 'Product added to Shopcart')
                return redirect('meals')

            else:
                newitem = ShopCart()
                newitem.user = request.user
                newitem.meal = mealid
                newitem.quantity = addquantity
                newitem.how_spicy = addspice
                newitem.order_no = cart[0].order_no
                newitem.items_paid = False
                newitem.save()
                messages.success(request, 'Product added to Shopcart')
                return redirect('meals')
        else:
            newcart = ShopCart()
            newcart.user = request.user
            newcart.meal = mealid
            newcart.quantity = addquantity
            newcart.how_spicy = addspice
            newcart.order_no = cart_code
            newcart.items_paid = False
            newcart.save()
            messages.success(request, 'Item has been added to your shopcart!')
            return redirect('meals')


@login_required(login_url='signin')
def cart(request):
    shopcart = ShopCart.objects.filter(user__username = request.user.username, items_paid = False) #whenever we use a filter, we iterate


    subtotal = 0
    vat = 0
    total = 0

    for item in shopcart:
        if item.meal.discount:
            subtotal += item.meal.discount * item.quantity
        else:
            subtotal += item.meal.price * item.quantity

    #vat is 7.5% of subtotal
    vat = 0.075 * subtotal

    #addition of vat and subtotal equals total
    total = subtotal + vat 


    context = {
        'shopcart':shopcart,
        'subtotal':subtotal,
        'vat':vat,
        'total':total,
    }
    return render(request, 'cart.html', context)

    return redirect('meals') 


@login_required(login_url='signin')
def remove_item(request):
    deleteitem = request.POST['deleteitem']
    ShopCart.objects.filter(pk=deleteitem).delete()
    messages.success(request, 'Items successfully deleted from your Shopcart!')
    return redirect('meals')


@login_required(login_url='signin')
def checkout(request):
    profile = Profile.objects.get(user__username= request.user.username)
    shopcart = ShopCart.objects.filter(user__username = request.user.username, items_paid = False)

    subtotal = 0
    vat = 0
    total = 0

    for item in shopcart:
        if item.meal.discount:
            subtotal += item.meal.discount * item.quantity
        else:
            subtotal += item.meal.price * item.quantity

    #vat is 7.5% of subtotal
    vat = 0.075 * subtotal

    #addition of vat and subtotal equals total
    total = subtotal + vat 

    context = {
        'shopcart': shopcart,
        'profile':profile,
        'total':total,
        # 'orderno': shopcart[0].order_no,
    }
    return render(request, 'checkout.html', context)


@login_required(login_url='signin')
# integrate to payment gateway, in this instance paystack 
def placeorder(request):
    if request.method == 'POST':
        # collect data to send to paystack
        # the api_key(application programming interphase key) and curl(call url) will be sourced from paystack site, 
        # paystack would give test secret key for testing, when you want to go live, paystack will give live key 
        # cburl (callback url), total, ref_num, order_num, emai provided by me in my application 
        api_key = 'sk_test_1bb25fe3a2658808a242baaff37ae05b3a9056ff'
        curl = 'https://api.paystack.co/transaction/initialize'
        cburl = 'http://44.203.38.186/paidorder'
        # cburl = 'http://localhost:1900/paidorder'
        # cburl = 'http://127.0.0.1/paidorder'
        ref_num = str(uuid.uuid4())
        total = float(request.POST['get_total']) * 100
        # order_num = request.POST['get_orderno']
        cartno = Profile.objects.get(user__username = request.user.username)
        order_num = cartno.cart_code 
        address = request.POST['address']
        phone = request.POST['phone']
        state = request.POST['state']
        user = User.objects.get(username = request.user.username)

        headers = {'Authorization': f'Bearer {api_key}'}
        data = {'reference':ref_num, 'order_number':order_num, 'amount':int(total), 'callback_url':cburl, 'email':user.email, 'currency':'NGN'}
        #collect data to send to paystack done
        # if currency is not stated, the default is dollar 


        #call to paystack
        try:
            r = requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, 'Network busy, please refresh and try again. Thank you.')
        else:
            transback = json.loads(r.text)
            rd_url = transback['data']['authorization_url']

            # take records oftransactions made 
            paidorder = PaidOrder()
            paidorder.user = user
            paidorder.total = total/100
            paidorder.cart_no = order_num
            paidorder.payment_code = ref_num
            paidorder.paid_item = True
            paidorder.first_name = user.first_name
            paidorder.last_name = user.last_name
            paidorder.save()


            shipping = Shipping()
            shipping.user = user
            # shipping.meal = 
            shipping.shipping_no = order_num
            shipping.paid_cart = True
            shipping.fname = user.first_name
            shipping.lname = user.last_name
            shipping.address = address
            shipping.phone = phone
            shipping.state = state
            shipping.save()
            # take records of transactions made done
            return redirect(rd_url)
        #call to paystack done, when transaction is successful it redirects to the callback page

    return redirect('checkout')


def paid_order(request):
    profile = Profile.objects.get(user__username = request.user.username)
    cart = ShopCart.objects.filter(user__username = request.user.username, items_paid = False)
    for item in cart:
        item.items_paid = True
        item.save()
    return render(request, 'thankyou.html')
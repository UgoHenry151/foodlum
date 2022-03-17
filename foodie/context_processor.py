from ast import For
from foodie.models import Variety
from shopcart.models import ShopCart


def dropdown(request):
    variet = Variety.objects.all()

    context = {
        'vee': variet,
    }

    return context


def cartpro(request):
    shopcart = ShopCart.objects.filter(user__username = request.user.username, items_paid = False)

    cartcount = 0

    for Item in shopcart:
        cartcount += Item.quantity 

    context = {
        'cartcount':cartcount,
    }

    return context 
import os
import json
import stripe
from django.shortcuts import render
from django.db.models import Avg, Max, Min, Sum
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from comics.models.profile_models import complete_comic, order, profile


stripe.api_key = settings.STRIPE_SECRET_KEY
#this is looping through all the comics in comics.json, creating each one as an object called complete_comic and appending them into a list called all_comics.
class ComicsView(TemplateView):
    template_name = '/src/profiles/templates/home.html'

# cart_comics = []
# total_price = 0


def parseComics(request):
    all_comics = complete_comic.objects.all()
    
    return render(request, '../templates/home.html', {'all_comics':all_comics})

@login_required
def add_to_cart(request, comic_id):
    comic_to_add = complete_comic.objects.get(id=comic_id)
    try:
        user_order = order.objects.get(user__user=request.user.id)
        user_order.comics.add(comic_to_add)

    except:
        user = profile.objects.get(user=request.user.id)
        user_order = order.objects.create(user=user)
        user_order.comics.add(comic_to_add)

    # context = {'cart_comics':cart_comics, 'total_price':total_price}
    # template = 'checkout.html'
    return HttpResponseRedirect('/checkout/')

def remove_from_cart(request, comic_id):

    comic_to_remove = complete_comic.objects.get(id=comic_id)
    try:
        user_order = order.objects.get(user__user=request.user.id)
        user_order.comics.remove(comic_to_remove)

    except:
        user = profile.objects.get(user=request.user.id)
        user_order = order.objects.create(user=user)
        user_order.comics.remove(comic_to_remove)
    return HttpResponseRedirect('/checkout/')

@login_required 
def checkout(request):

    current_order = order.objects.get(user__user=request.user.id)
    comics = current_order.comics.all()
    comic_price_sum = current_order.comics.aggregate(Sum('price')).get('price__sum', 0.00)
    total_price = comic_price_sum


    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = request.user.userstripe.stripe_id
    if request.method == 'POST':
        # Token is created using Stripe.js or Checkout!
        # Get the payment token submitted by the form:
        token = request.POST['stripeToken'] # Using Flask
        # print("!!!!!!!STRIPETOKEN: ", stripeToken)
        try:
        # Charge the user's card:
            customer = stripe.Customer.retrieve(customer_id)
            customer.sources.create(source=token)
            charge = stripe.Charge.create(
              amount=1000,
              currency="usd",
              customer = customer,
              description="Example charge",
            )
        except stripe.error.CardError as e:
            #The card has been declined
            pass
    context = {'publishKey':publishKey, 'current_order':current_order, 'comics':comics,'total_price':total_price}
    template = 'checkout.html'
    return render(request, template, context)

#this is my about page, or where the customer will learn about the company
def success(request):
    context = {}
    template = 'success.html'
    return render(request, template, context)




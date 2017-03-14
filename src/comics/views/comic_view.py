import os
import json
import stripe
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

stripe.api_key = settings.STRIPE_SECRET_KEY
#this is looping through all the comics in comics.json, creating each one as an object called complete_comic and appending them into a list called all_comics.
class ComicsView(TemplateView):
    template_name = '/src/profiles/templates/home.html'

all_comics = []
complete_comic = {}
cart_comics = []
total_price = 0


def parseComics(request):

    try:
        with open("../comics.json", "r") as files:
            comic_data = json.load(files)
            comics = comic_data["results"]
            for comic in comics:
                complete_comic = {
                    'comic_id':comic["id"],
                    'comic_title':comic["title"],
                    'description':comic["description"],
                    'price':round(comic["prices"][0]["price"],2),
                    'comic_cover':comic["thumbnail"]["path"] + "." + comic["thumbnail"]["extension"]
                }
                all_comics.append(complete_comic)
                # print("ALL COMICS:  ", all_comics)

    except: 
        print("HAPPPPPPYYPYPPPYY") 

    return render(request, '../templates/home.html', {'all_comics':all_comics})

def add_to_cart(request, comic_id):
    for comic in all_comics:
        # print("COMIC: ", comic)
        if int(comic['comic_id']) == int(comic_id):
            total_price = calculate_price(request, comic['price'])
            cart_comics.append(comic)
            break

    context = {'cart_comics':cart_comics, 'total_price':total_price}
    template = 'checkout.html'
    return HttpResponseRedirect('/checkout/')

def calculate_price(request, comic_price):
    global total_price
    print("!!!!!!COMIC PRICE", comic_price)
    total_price += comic_price
    print("!!!!TOTAL PRICE", total_price)
    return total_price

def lower_price(request, comic_price):
    global total_price
    print("!!!!!!COMIC PRICE", comic_price)
    total_price -= comic_price
    print("!!!!TOTAL PRICE", total_price)
    return total_price

def remove_from_cart(request, comic_id):
    for comic in all_comics:
        # print("COMIC: ", comic)
        if int(comic['comic_id']) == int(comic_id):
            total_price = lower_price(request, comic['price'])
            cart_comics.remove(comic)
            break

    context = {'cart_comics':cart_comics, 'total_price':total_price}
    template = 'checkout.html'
    return HttpResponseRedirect('/checkout/')

@login_required 
def checkout(request):

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
    context = {'publishKey':publishKey, 'cart_comics':cart_comics,'total_price':total_price}
    template = 'checkout.html'
    return render(request, template, context)

#this is my about page, or where the customer will learn about the company
def success(request):
    context = {}
    template = 'success.html'
    return render(request, template, context)




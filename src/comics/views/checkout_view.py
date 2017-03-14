from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

# @login_required 
# def checkout(request):
#     publishKey = settings.STRIPE_PUBLISHABLE_KEY
#     customer_id = request.user.userstripe.stripe_id
#     if request.method == 'POST':
#         # Token is created using Stripe.js or Checkout!
#         # Get the payment token submitted by the form:
#         token = request.POST['stripeToken'] # Using Flask
#         try:
#         # Charge the user's card:
#             customer = stripe.Customer.retrieve(customer_id)
#             customer.sources.create(source=token)
#             charge = stripe.Charge.create(
#               amount=1000,
#               currency="usd",
#               customer = customer,
#               description="Example charge",
#             )
#         except stripe.error.CardError as e:
#             #The card has been declined
#             pass
#     context = {'publishKey':publishKey}
#     template = 'checkout.html'
#     return render(request, template, context)
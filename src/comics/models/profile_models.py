from django.db import models
from django.conf import settings
from django.db import models
from allauth.account.signals import user_logged_in, user_signed_up
import stripe
from django.db.models import Avg, Max, Min

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your models here.

#profile is used to store the customers information
class profile(models.Model):
    name = models.CharField(max_length=120)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    description = models.TextField(default='description default text')


    def __str__(self):
        return self.name

class complete_comic(models.Model):
    comic_id = models.IntegerField()
    comic_title = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000, null=True, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comic_cover = models.ImageField()

class order(models.Model):
    user = models.ForeignKey(profile, on_delete=models.CASCADE)
    comics = models.ManyToManyField(complete_comic)

class userStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username

#this is created a user if someone registers, as well as attaching them to a stripId
def stripeCallback(sender, request, user, **kwargs):
    user_stripe_account, created = userStripe.objects.get_or_create(user = user)
    if created:
        print('created for %s'%(user.username))
    if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
        new_stripe_id = stripe.Customer.create(email = user.email)
        user_stripe_account.stripe_id = new_stripe_id['id']
        user_stripe_account.save()

def profileCallback(sender, request, user, **kwargs):
    userProfile, is_created = profile.objects.get_or_create(user = user)
    if is_created:
        userProfile.name = user.username
        userProfile.save()

user_logged_in.connect(stripeCallback)
user_signed_up.connect(stripeCallback)
user_signed_up.connect(profileCallback)



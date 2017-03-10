from django.contrib import admin

# Register your models here.
from .models.profile_models import profile, userStripe
#this is adding our profile class directly to the admin page so I can add profiles through the django console
class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = profile

admin.site.register(profile, profileAdmin)

class userStripeAdmin(admin.ModelAdmin):
    class Meta:
        model = userStripe

admin.site.register(userStripe, userStripeAdmin)

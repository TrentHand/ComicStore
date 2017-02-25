from django.contrib import admin

# Register your models here.
from .models import profile
#this is adding our profile class directly to the admin page so I can add profiles through the django console
class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = profile

admin.site.register(profile, profileAdmin)
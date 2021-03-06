"""ComicStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from comics.views import checkout_view, contact_view, profile_view, comic_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', comic_view.parseComics, name='home'),
    url(r'^about/$', profile_view.about, name='about'),
    url(r'^profile/$', profile_view.userProfile, name='profile'),
    # url(r'^checkout/$', checkout_view.checkout, name='checkout'),
    url(r'^add_comic/(?P<comic_id>\d+)/', comic_view.add_to_cart, name='add_comic'),
    url(r'^remove_comic/(?P<comic_id>\d+)/', comic_view.remove_from_cart, name='remove_comic'),
    url(r'^checkout/', comic_view.checkout, name='checkout'),
    url(r'^contact/$', contact_view.contact, name='contact'),
    url(r'^success/$', comic_view.success, name='success'),
    url(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
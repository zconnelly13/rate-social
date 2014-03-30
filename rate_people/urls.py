from django.conf.urls import patterns, include, url
from database.views import add_rating, add_user

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rate_people.views.home', name='home'),
    # url(r'^rate_people/', include('rate_people.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addRating/',add_rating),
    url(r'^addUser/',add_user),
)

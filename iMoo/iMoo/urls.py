from django.conf.urls import patterns, include, url
from iMoo.views import display_root

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iMoo.views.home', name='home'),
    # url(r'^iMoo/', include('iMoo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', display_root),
    url(r'^app/', include('dairy_farm.urls', namespace='dairy_farm')),
)

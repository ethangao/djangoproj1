from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import app1

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj1.views.home', name='home'),
    # url(r'^proj1/', include('proj1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app1.views.home'),
    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^register$', 'app1.views.register'),
    url(r'^addtopic$', 'app1.views.addtopic'),
    url(r'^adddiscuss$', 'app1.views.adddiscuss'),
)
urlpatterns += staticfiles_urlpatterns()

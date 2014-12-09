from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'craiggle.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^django-rq/', include('django_rq.urls')),
)

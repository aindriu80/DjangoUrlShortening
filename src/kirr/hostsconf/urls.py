from django.conf.urls import url

from .views import wildcard_redirect
urlpatterns = [
    url(r'^(?P<path>.*)', wildcard_redirect),  
]

'''
from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    #host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
    host(r'(?!www).*', 'kirr.hostsconf.urls', name='wildcard'),
)
'''
 
 

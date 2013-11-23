"""
URL patterns and routing for the Deis web app.
"""

from __future__ import unicode_literals

from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url


urlpatterns = patterns(
    'web.views',
    url(r'^$', 'home', name='home'),
    url(r'^app/(?P<id>[-_\w]+)$', 'app', name='apps'),
    url(r'^captcha/', include('captcha.urls'))
)

"""
View classes for presenting Deis web pages.
"""

from django.shortcuts import render
from django.contrib import messages
from api.models import App
from api.models import Formation
from web.forms import CaptchaForm
from django.conf import settings

import time


def home(request):
    """The home page with a list of apps on"""
    apps = App.objects.all()
    formation = Formation.objects.get(id='swanson')
    return render(request, 'web/home.html', {
        'page': 'home',
        'apps': apps,
        'formation': formation,
    })


def app(request, id):
    """Return the user's apps web page."""

    app = App.objects.get(id=id)

    if request.POST:
        form = CaptchaForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            app.addCredits(settings.CREDITS_PER_CAPTCHA)
            time.sleep(2)  # Gotta be a better way of waiting for the transaction to complete...
            messages.success(
                request,
                "{} credits successfully donated.".format(settings.CREDITS_PER_CAPTCHA)
            )
    else:
        form = CaptchaForm()

    return render(request, 'web/app.html', {
        'page': 'app',
        'app': app,
        'containers': app.container_set.all(),
        'form': form,
        'settings': settings,
        'pool_cut': "{}%".format(settings.POOL_CUT * 100),
        'danabox_cut': "{}%".format(settings.DANABOX_CUT * 100),
    })

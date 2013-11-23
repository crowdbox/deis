"""
View classes for presenting Deis web pages.
"""

from django.shortcuts import render
from api.models import App
from web.forms import CaptchaForm


def home(request):
    """The home page with a list of apps on"""
    apps = App.objects.all()
    return render(request, 'web/home.html', {
        'page': 'home',
        'apps': apps,
    })


def app(request, id):
    """Return the user's apps web page."""
    app = App.objects.get(id=id)

    if request.POST:
        form = CaptchaForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            app.addCredits(60)
    else:
        form = CaptchaForm()

    return render(request, 'web/app.html', {
        'page': 'app',
        'app': app,
        'containers': app.container_set.all(),
        'form': form,
    })

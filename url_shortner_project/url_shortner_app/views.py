import random
import string
from django.shortcuts import render, redirect
from django.http import Http404
from .models import URL

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    return short_url

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        # Check if the URL already exists in the database
        try:
            url = URL.objects.get(original_url=original_url)
        except URL.DoesNotExist:
            # If the URL doesn't exist, generate a new short URL and save it
            short_url = generate_short_url()
            url = URL.objects.create(original_url=original_url, short_url=short_url)
        return render(request, 'url_shortner_app/shortened_url.html', {'short_url': url.short_url})
    return render(request, 'url_shortner_app/shorten_url.html')

def redirect_to_original(request, short_url):
    try:
        url = URL.objects.get(short_url=short_url)
        return redirect(url.original_url)
    except URL.DoesNotExist:
        raise Http404

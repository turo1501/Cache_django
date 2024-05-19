from django.shortcuts import render, redirect
from .models import *
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def home(request):
	recipes = Recipe.objects.all()
	context = {'recipes': recipes}
	return render(request, "home.html", context)


def view_recipe(request, id):
	if cache.get(id):
		print("Data From Cache")
		recipe = cache.get(id)
	else:
		try:
			recipe = Recipe.objects.get(id=id)
			cache.set(id, recipe, CACHE_TTL)
			print("Data From DB")
		except Recipe.DoesNotExist:
			return redirect('/')
	context = {'recipe': recipe}
	return render(request, "view.html", context)

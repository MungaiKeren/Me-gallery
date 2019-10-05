from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import *


# Create your views here.
def index(request):
    title = 'MyGallery'
    today = dt.datetime.today()
    all_images = Image.get_images()
    locations = Location.get_location()
    categories = Category.get_all_categories()
    param = {
        "title": title,
        "today": today,
        "all_images": all_images,
        "locations": locations,
        "categories": categories
    }
    return render(request, 'index.html', param)


def display_location(request, img_location__id):
    locations = Location.get_location()
    found_locations = Image.objects.filter(img_location__id=img_location__id)
    param = {
        "locations": locations,
        "found_locations": found_locations,
    }
    return render(request, 'locations.html', param)


def category(request):
    categorize = Category.get_all_categories()
    locations = Location.get_location()
    all_images = Image.get_images()
    param = {
        "categorize": categorize,
        "locations": locations,
        "all_images": all_images
    }
    return render(request, 'category.html', param)

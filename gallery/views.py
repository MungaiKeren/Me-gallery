from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import *


# Create your views here.
def index(request):
    title = 'MyGallery'
    today = dt.datetime.today()
    all_images = Image.get_images()
    param = {
        "title": title,
        "today": today,
        "all_images": all_images,
    }
    return render(request, 'index.html', param)


def display_location(request, img_location_id):
    locations = Location.get_location()
    all_images = Image.get_images()
    found_locations = Image.objects.filter(img_location__id=img_location_id)
    param = {
        "locations": locations,
        "found_locations": found_locations,
        "all_images": all_images
    }
    return render(request, 'locations.html', param)


def category(request, img_category_id):
    found_categories = Image.objects.filter(img_category__id=img_category_id)
    param = {
        "found_categories": found_categories
    }
    return render(request, 'category.html', param)


def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        params = {
            "images": searched_images,
            "message": search_term
        }
        return render(request, 'search.html', params)

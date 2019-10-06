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
    param = {
        "title": title,
        "today": today,
        "all_images": all_images,
        "locations": locations,
    }
    return render(request, 'index.html', param)


def display_location(request, id):
    locations = Location.get_location()
    images = Image.objects.filter(img_location__id=id)
    param = {
        "locations": locations,
        "images": images
    }
    return render(request, 'locations.html', param)


def category(request, img_category_id):
    found_categories = Image.objects.filter(img_category__id=img_category_id)
    param = {
        "found_categories": found_categories
    }
    return render(request, 'category.html', param)


def search_results(request):
    locations = Location.get_location()
    images = Image.objects.all()
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_category(search_term)
        message = f"{search_term}"
        params = {
            "message": message,
            "category": searched_category,
            "images": images,
            "locations": locations
        }
        return render(request, 'search.html', params)

    else:
        message = "Search not found"
        return render(request, 'index.html', {"message": message, "locations": locations})

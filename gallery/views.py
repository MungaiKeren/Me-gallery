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
    categorize = Category.get_all_categories()
    locations = Location.get_location()
    all_images = Image.get_images()
    found_categories = Image.objects.filter(img_category__id=img_category_id)
    param = {
        "categorize": categorize,
        "locations": locations,
        "all_images": all_images,
        "found_categories": found_categories
    }
    return render(request, 'category.html', param)


def search_results(request):
    
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        searched_category = Category.search_by_category(search_term)
        message = f"{search_term}"
        param = {
            "message": message,
            "categories": searched_category,

        }
        return render(request, 'search.html', param)
    else:
        message = "You haven't searched for any categories"
        return render(request, "index.html", {"message": message})

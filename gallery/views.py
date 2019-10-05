from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image, Location, Category


# Create your views here.
def index(request):
    title = 'MyGallery'
    today = dt.datetime.today()
    all_images = Image.get_images()
    param = {
        "title": title,
        "today": today,
        "all_images": all_images
    }
    return render(request, 'index.html', param)

from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt


# Create your views here.
def index(request):
    title = 'MyGallery'
    today = dt.datetime.today()
    return render(request, 'index.html', {"title": title, "today": today})


from django.shortcuts import render
import requests

# Create your views here.
def index(request):

    return render(request, 'index.html')


def allnews(request):
    records = {}
    urls = requests.get("https://inshorts.me/news/all?offset=0&limit=21")
    allnews_data = urls.json()
    records['allnewsdata'] = allnews_data

    return render(request, 'allnews.html', records)

def entnews(request):
    records = {}
    urls = requests.get("https://inshorts.me/news/topics/entertainment")
    entnews_data = urls.json()
    records['entnewsdata'] = entnews_data

    return render(request, 'entnews.html', records)

def sciencenews(request):
    records = {}
    urls = requests.get("https://inshorts.me/news/topics/science")
    sciencenews_data = urls.json()
    records['sciencenewsdata'] = sciencenews_data

    return render(request, 'sciencenews.html', records)

def sportsnews(request):
    records = {}
    urls = requests.get("https://inshorts.me/news/topics/sports")
    sportsnews_data = urls.json()
    records['sportsnewsdata'] = sportsnews_data

    return render(request, 'sportsnews.html', records)


def topnews(request):
    records = {}
    urls = requests.get("https://inshorts.me/news/top?offset=0&limit=21")
    topnews_data = urls.json()
    records['topnewsdata'] = topnews_data

    return render(request, 'topnews.html', records)


def trendingnews(request):
    records = {}
    urls = requests.get("https://inshorts.me/news/trending?offset=0&limit=21")
    trendingnews_data = urls.json()
    records['trendingnewsdata'] = trendingnews_data

    return render(request, 'trendingnews.html', records)


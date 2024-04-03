from django.shortcuts import render
import requests
#API_KEY='0a489ff65f5b432cba6fec5295ce61eb'
# Create your views here.

def home(request):
    country=request.GET.get('country')
    category=request.GET.get('category')
    if country:
        url=f'https://newsapi.org/v2/top-headlines?country={country}&apiKey=0a489ff65f5b432cba6fec5295ce61eb'
        response=requests.get(url)
        data=response.json()
        articles=data['articles']
    else:
        url=f'https://newsapi.org/v2/top-headlines?category={category}&apiKey=0a489ff65f5b432cba6fec5295ce61eb'
        response=requests.get(url)
        data=response.json()
        articles=data['articles']
    context={
        'articles':articles
    }
    return render(request,'home.html',context)

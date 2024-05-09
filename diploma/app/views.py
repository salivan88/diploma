from django.http import HttpResponse
from django.shortcuts import render
import requests


# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request): 
    return render(request, 'profile.html')

def watched(request): 
    return render(request, 'watched.html')

# def tmdb_movies(request):
#     api_key = '7f540cdc422c17adc3781b8227d0b71c'
#     url = 'https://api.themoviedb.org/3/movie/popular'

#     params = {
#         'api_key': api_key,
#         'language': 'uk',
#         'page': 1,
#     }

#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         movies = data.get('results', [])
#         return render(request, 'index.html', { 'movies':movies})
#     else:
#         return HttpResponse('Failed to fetch data from TMDb', status=response.status_code)



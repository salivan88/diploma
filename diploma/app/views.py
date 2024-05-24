from django.http import HttpResponse, JsonResponse
import requests
from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserMovie
from django.core.serializers import serialize

from .recommendations import recommend_movies_for_user



def index(request):
    return render(request, 'index.html')

def rec(request): 
    user_id = request.user.id
    recommendations = recommend_movies_for_user(user_id)
    api_key = '7f540cdc422c17adc3781b8227d0b71c'

    movies = []
    for movie_id in recommendations:
        movie_details = get_movie_details(movie_id, api_key)
        if movie_details:
            movies.append(movie_details)

    context = {
        'movies': movies
    }
    return render(request, 'profile.html', context)

def get_movie_details(movie_id, api_key):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def profile(request): 
    return render(request, 'profile.html')

def watched(request): 
    user_id = request.user.id
    user_movies = UserMovie.objects.filter(user_id=user_id)
    user_movies_json = serialize('json', user_movies) 
    
    return render(request, 'watched.html', {'user_movies_json': user_movies_json})

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
    else:
        form = CreateUserForm()

    error_messages = form.errors.as_data()
    context = {'registerform': form, 'errors': error_messages}

    return render(request, 'register.html', context=context)


def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("/profile")


    context = {'loginform':form}

    return render(request, 'my-login.html', context=context)


def user_logout(request):

    auth.logout(request)

    return redirect("/")

@csrf_exempt
def add_user_movie(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id') 
        rating = request.POST.get('rating') 

        if movie_id and rating:
            UserMovie.objects.create(movie_id=movie_id, user=request.user, rating=rating)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Movie ID not provided'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    




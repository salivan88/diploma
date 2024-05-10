from django.http import HttpResponse
import requests
from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'index.html')

def profile(request): 
    return render(request, 'profile.html')

def watched(request): 
    return render(request, 'watched.html')

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("my-login")


    context = {'registerform':form}

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

                return redirect("dashboard")


    context = {'loginform':form}

    return render(request, 'my-login.html', context=context)


def user_logout(request):

    auth.logout(request)

    return redirect("/")



@login_required(login_url="my-login")
def dashboard(request):

    return render(request, 'dashboard.html')







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



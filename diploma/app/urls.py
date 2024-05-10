from django.urls import path
from app.views import *

urlpatterns = [
    path('', index),
    path('profile', profile),
    path('watched', watched),


    path('register', register, name="register"),

    path('my-login', my_login, name="my-login"),

    path('dashboard', dashboard, name="dashboard"),

    path('user-logout', user_logout, name="user-logout"),
]
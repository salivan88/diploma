from django.urls import path
from app.views import *

urlpatterns = [
    path('', index),
    path('profile', profile, name="profile"),
    path('watched', watched),


    path('register', register, name="register"),

    path('my-login', my_login, name="my-login"),

    path('user-logout', user_logout, name="user-logout"),

    path('add_user_movie/', add_user_movie, name='add_user_movie'),
    
]
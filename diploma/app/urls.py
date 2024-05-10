from django.urls import path
from app.views import *

urlpatterns = [
    path('', index),
    path('profile', profile),
    path('watched', watched)
]
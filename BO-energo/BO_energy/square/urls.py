from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', math_square, name = 'square'),
]

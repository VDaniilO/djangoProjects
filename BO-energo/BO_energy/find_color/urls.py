from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', color_finder, name = 'color_finder'),
    path('all_color/', out_all_color, name = 'all_color'),
]

from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('expPage/', adminUsr, name = 'home'),
    path('profile/<str:usrInfo>', profileUsr, name = 'profile'),
    path('regionFilter/<int:region_id>', regionUsrFilter, name = 'regionUsr')
]

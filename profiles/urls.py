from django.urls import path
from .views import *

# app_name = 'posts'
urlpatterns = [
    path('dashboard', profile_page, name='dashboard_profile'),
]

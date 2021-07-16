from django.urls import path
from . import views


app_name = 'core'

ulrpatterns = [
    path('', views.api_redirect, name='api_redirect'),
]
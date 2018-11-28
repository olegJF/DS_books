from django.urls import path
from .views import home

app_name = 'http_head'
urlpatterns = [
    path('', home, name='home'),
]
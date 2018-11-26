from django.urls import path
from .views import home, BookCreate

app_name = 'books'
urlpatterns = [
    path('create/', BookCreate.as_view(), name='create'),
    path('', home, name='home'),
]
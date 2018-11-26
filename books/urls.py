from django.urls import path
from .views import home, BookCreate, BookUpdate

app_name = 'books'
urlpatterns = [
    path('create/', BookCreate.as_view(), name='create'),
    path('update/<int:pk>/', BookUpdate.as_view(), name='update'),
    path('', home, name='home'),
]
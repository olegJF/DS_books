from django.urls import path
from .views import home, BookCreate, BookUpdate, BookDelete

app_name = 'books'
urlpatterns = [
    path('create/', BookCreate.as_view(), name='create'),
    path('update/<int:pk>/', BookUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', BookDelete.as_view(), name='delete'),
    path('', home, name='home'),
]

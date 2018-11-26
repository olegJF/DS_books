from django.shortcuts import render
from .models import Book

def home(request):
    qs = Book.objects.all()
    context = {}
    context['objects_list'] = qs
    return render(request, 'books/home.html', context)
    
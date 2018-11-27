from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView
from .models import Book
from .forms import BookForm

def home(request):
    sort = request.GET.get('sort', 'desc')
    if sort == 'desc':
        qs = Book.objects.sort()
    else:
        qs = Book.objects.sort('asc')
    context = {}
    context['objects_list'] = qs
    return render(request, 'books/home.html', context)
    
    
class BookCreate(SuccessMessageMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create.html'
    success_url = reverse_lazy('books:home')
    success_message = "Книга была успешно создан!"
    

class BookUpdate(SuccessMessageMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create.html'
    success_url = reverse_lazy('books:home')
    success_message = "Редактирование прошло успешно!"

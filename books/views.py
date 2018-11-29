import logging
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Book
from .forms import BookForm
from django.contrib import messages

logger = logging.getLogger(__name__)


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
    success_message = "Книга была успешно создана!"
    
    def post(self, request, *args, **kwargs):
        logger.info('The book was created!')
        return super().post(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BookUpdate(SuccessMessageMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create.html'
    success_url = reverse_lazy('books:home')
    success_message = "Редактирование прошло успешно!"
    
    def post(self, request, *args, **kwargs):
        logger.info('The book was updated!')
        return super().post(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
        

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:home')
        
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Книга была успешно удалена!')
        logger.info('The book was deleted!')
        return self.post(request, *args, **kwargs)

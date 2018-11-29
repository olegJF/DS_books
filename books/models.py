from django.db import models
from django.utils import timezone


class BookQuerySet(models.query.QuerySet):
    
    def sort(self, how_to='desc'):
        if how_to == 'desc':
            return self.order_by('publish_date')
        else:
            return self.order_by('-publish_date')
        
        
class BookManager(models.Manager):
    
    def get_queryset(self):
        return BookQuerySet(self.model, using=self._db)

    def sort(self, how_to='desc'):
        return self.get_queryset().sort(how_to)


class Book(models.Model):
    book_title = models.CharField(max_length=255, verbose_name='Название книги')
    authors_info = models.TextField(verbose_name='Информация об авторах')
    isbn = models.CharField(max_length=20, unique=True,
                            verbose_name='ISBN книги')
    price = models.DecimalField(max_digits=10, decimal_places=2, 
                                verbose_name='Цена книги')
    publish_date = models.DateField(default=timezone.now, 
                                    verbose_name='Дата публикации')
    objects = BookManager()
                                                    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['book_title']
        
    def __str__(self):
        return self.book_title


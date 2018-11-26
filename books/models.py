from django.db import models


class Book(models.Model):
    book_title = models.CharField(max_length=255, verbose_name='Название книги')
    authors_info = models.TextField(verbose_name='Информация об авторах')
    isbn = models.CharField(max_length=20, unique=True,
                                        verbose_name='ISBN книги')
    price = models.DecimalField(max_digits=10, decimal_places=2, 
                                                    verbose_name='Цена книги')
    publish_date = models.DateTimeField(verbose_name='Дата публикации')
                                                    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['book_title']
        
    def __str__(self):
        return self.book_title
        
        
    
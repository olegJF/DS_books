from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    book_title = forms.CharField(label='Название', required=True,
                           widget=forms.TextInput(
                               attrs={"class": 'form-control'}))
    authors_info = forms.CharField(label='Информация об авторах',
                           widget=forms.TextInput(
                               attrs={"class": 'form-control'}))
    isbn = forms.CharField(label='ISBN',
                           widget=forms.TextInput(
                               attrs={"class": 'form-control'}))
    price = forms.DecimalField(label='Цена', required=True,
                                     widget=forms.NumberInput(
                                         attrs={"class": 'form-control'}))    
    class Meta(object):
        model = Book
        fields = ('book_title', 'authors_info', 'isbn', 'price')

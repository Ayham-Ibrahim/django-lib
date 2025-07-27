from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .models import Book
# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books' # the name of variable that contains data

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books' # the name of variable that contains data

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books' # the name of variable that contains data
    
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_details.html'
    context_object_name = 'book' # the name of variable that contains data
    
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_list.html'
    success_url = reverse_lazy('book-list')
    
    
    
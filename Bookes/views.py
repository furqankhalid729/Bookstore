from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import *
from django.db.models import Q
# Create your views here.

class book_display(LoginRequiredMixin,ListView):
    model=book
    template_name ='books/book_list.html'


class book_detail(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model=book
    template_name = 'books/book_detail.html'
    permission_required = 'books.special_status'

class SearchResultsListView(ListView): # new
    model = book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'


    def get_queryset(self):
        query=self.request.GET.get('q')
        return book.objects.filter(Q(Name__icontains=query)|Q(author__icontains=query))
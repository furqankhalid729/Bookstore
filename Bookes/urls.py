from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',book_display.as_view(),name='book_list'),
    path('<uuid:pk>',book_detail.as_view(),name='book_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results')
]
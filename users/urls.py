from django.contrib import admin
from django.urls import path,include
from .views import SignupPageView
urlpatterns = [
    path('accounts/signup', SignupPageView.as_view(), name='signup'),

]
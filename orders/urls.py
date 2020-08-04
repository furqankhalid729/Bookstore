
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', OrdersPageView.as_view(), name='orders'),
    path('charge/',charge,name='charge'),
]

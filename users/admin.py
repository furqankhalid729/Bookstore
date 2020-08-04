from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import *
from.models import *

# Register your models here.
class customUserAdmin(UserAdmin):
    add_form = customUserCreationForm
    form = customUserChangeForm
    model=get_user_model()
    list_display = ['email','username','age']

admin.site.register(customeruser, customUserAdmin)

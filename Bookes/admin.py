from django.contrib import admin
from .models import *
# Register your models here.

class reviewInline(admin.TabularInline):
    model = review

class bookAdmin(admin.ModelAdmin):

    inlines = [reviewInline]
    list_display = ('Name','author','Price')


admin.site.register(book,bookAdmin)
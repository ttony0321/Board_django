from django.contrib import admin
from .models import Board

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'writer',
        'views',
        'registered_date'
    )
    search_fields = ('title', 'content',)#admin 검색기능

admin.site.register(Board, BoardAdmin)
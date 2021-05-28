from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('userid', 'password', 'email', 'level', 'registered_dttm')

    search_fields = ('userid',)

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)#Admin 페이지 GROUP 삭제

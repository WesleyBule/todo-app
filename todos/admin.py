from django.contrib import admin
from .models import Todo
from django.contrib.auth.models import User

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title' , 'created' ,'deadline', 'completed']

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
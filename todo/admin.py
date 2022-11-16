from django.contrib import admin

from todo.models  import  Todo

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = ['tittle', 'body', 'user']
    list_filter = ['tittle', 'date']




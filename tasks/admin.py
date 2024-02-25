from django.contrib import admin
from .models import Task, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Task)
class TasksAdmin(SummernoteModelAdmin):

    list_display = ('title', 'description', 'priority', 'completed', 'user')
    search_fields = ['title', 'description', 'user']
    list_filter = ('description', 'priority', 'completed', 'user')
    prepopulated_fields = {'title': ()}
    summernote_fields = ('title',)
    
@admin.register(Category)
class CategoriesAdmin(SummernoteModelAdmin):

    list_display = ('category_name', 'user')
    search_fields = ['category_name', 'user']
    list_filter = ('user',)
    prepopulated_fields = {'category_name': ()}
    summernote_fields = ('category_name',)


# Register your models here.

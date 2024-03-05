from django.contrib import admin
from .models import Task, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Task)
class TasksAdmin(SummernoteModelAdmin):

    list_display = ('reviewed', 'title', 'description', 'user', 'created_at', 'due_at')
    search_fields = ['title', 'description', 'user']
    list_filter = ('reviewed', 'user', 'created_at', 'completed', 'priority')
    prepopulated_fields = {'title': ()}
    summernote_fields = ('title',)
    
    actions = ['mark_as_reviewed'] # Adds the custom action
    
    def mark_as_reviewed(self, request, queryset):
        queryset.update(reviewed=True)
    mark_as_reviewed.short_description = "Review selected tasks"
    
@admin.register(Category)
class CategoriesAdmin(SummernoteModelAdmin):

    list_display = ('category_name', 'user')
    search_fields = ['category_name', 'user']
    list_filter = ('user',)
    prepopulated_fields = {'category_name': ()}
    summernote_fields = ('category_name',)


# Register your models here.

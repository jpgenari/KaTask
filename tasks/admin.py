from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Task, Category


@admin.register(Task)
class TasksAdmin(SummernoteModelAdmin):
    '''
    Uses Summernote to display richer admin pane with extra filters and list
    display Tasks elements.
    '''

    list_display = (
        'reviewed', 'title', 'description', 'user', 'created_at', 'due_at'
        )
    search_fields = ['title', 'description', 'user']
    list_filter = ('reviewed', 'user', 'created_at', 'completed', 'priority')
    prepopulated_fields = {'title': ()}
    summernote_fields = ('title',)

    actions = ['mark_as_reviewed']  # Adds the custom action to Admin panel

    def mark_as_reviewed(self, request, queryset):
        '''
        Adds a custom action to admin panel, option to edit multiple items
        instead of only deleting.
        '''

        queryset.update(reviewed=True)
    mark_as_reviewed.short_description = "Review selected tasks"


@admin.register(Category)
class CategoriesAdmin(SummernoteModelAdmin):
    '''
    Uses Summernote to display richer admin pane with extra filters and list
    display Categories elements.
    '''

    list_display = ('category_name', 'user')
    search_fields = ['category_name', 'user']
    list_filter = ('user',)
    prepopulated_fields = {'category_name': ()}
    summernote_fields = ('category_name',)

# Register your models here.

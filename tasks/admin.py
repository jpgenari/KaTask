from django.contrib import admin
from .models import Task
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Task)
class TasksAdmin(SummernoteModelAdmin):

    list_display = ('title', 'description', 'priority', 'completed', 'user')
    search_fields = ['title', 'description', 'user']
    list_filter = ('description', 'priority', 'completed', 'user')
    prepopulated_fields = {'priority': ('title',)}
    summernote_fields = ('title',)


# Register your models here.

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Features, HowToUse, UserFeedback


@admin.register(Features)
class FeaturesAdmin(SummernoteModelAdmin):
    '''
    Uses Summernote to display richer admin pane with extra filters and list
    display Features elements.
    '''

    list_display = ('title', 'icon', 'content', 'display_order', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('updated_on', 'display_order')
    prepopulated_fields = {'title': ()}
    summernote_fields = ('title',)


@admin.register(HowToUse)
class HowToUseAdmin(SummernoteModelAdmin):
    '''
    Uses Summernote to display richer admin pane with extra filters and list
    display HowToUse elements.
    '''

    list_display = ('title', 'icon', 'content', 'display_order', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('updated_on', 'display_order')
    prepopulated_fields = {'title': ()}
    summernote_fields = ('title',)


@admin.register(UserFeedback)
class UserFeedbackAdmin(SummernoteModelAdmin):
    '''
    Uses Summernote to display richer admin pane with extra filters and list
    display UserFeedback elements.
    '''

    list_display = ('content', 'author', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('updated_on', 'content')
    prepopulated_fields = {'content': ()}
    summernote_fields = ('content',)

# Register your models here.

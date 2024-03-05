from django.contrib import admin
from .models import Features, HowToUse, UserFeedback
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Features)
class FeaturesAdmin(SummernoteModelAdmin):

    list_display = ('title', 'icon', 'content', 'display_order', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('updated_on', 'display_order')
    prepopulated_fields = {'title': ()}
    summernote_fields = ('title',)
    
@admin.register(HowToUse)
class HowToUseAdmin(SummernoteModelAdmin):

    list_display = ('title', 'icon', 'content', 'display_order', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('updated_on', 'display_order')
    prepopulated_fields = {'title': ()}
    summernote_fields = ('title',)
    
@admin.register(UserFeedback)
class UserFeedbackAdmin(SummernoteModelAdmin):

    list_display = ('content', 'author', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('updated_on', 'content')
    prepopulated_fields = {'content': ()}
    summernote_fields = ('content',)

# Register your models here.

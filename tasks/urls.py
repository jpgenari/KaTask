from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('tasks/', login_required(views.display_tasks), name='tasks'),
    path('category/', login_required(views.display_categories), name='categories'),
    path('category/<int:category_id>/', login_required(views.category_detail), name='category_detail'),
    path('create-task/', login_required(views.create_task), name='create_task'),
    path('create-category/', login_required(views.create_category), name='create_category'),
    path('edit-task/<int:task_id>/', login_required(views.edit_task), name='edit_task'),
    path('complete-task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('undo_complete-task/<int:task_id>/', views.undo_complete_task, name='undo_complete_task'),
    path('edit-category/<int:category_id>/', login_required(views.edit_category), name='edit_category'),
    path('delete-task/<int:task_id>/', login_required(views.delete_task), name='delete_task'),
    path('delete-category/<int:category_id>/', login_required(views.delete_category), name='delete_category'),
]

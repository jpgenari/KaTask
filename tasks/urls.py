from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('category/', views.category_list, name='category_list'),
    path('create/', views.create_task, name='create_task'),
    path('create_category/', views.create_category, name='create_category'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('edit/category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('delete/category/<int:category_id>/', views.delete_category, name='delete_category'),
]

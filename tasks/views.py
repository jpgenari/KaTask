from django.shortcuts import render, redirect
from .models import Task, Category
from .forms import TaskForm, CategoryForm

# Create your views here.

def category_list(request):
    '''
    View function that displays list of categories associated with current logged user.
    Retrieves all categories associated with logged user from database and renders template
    to display the categories.
    '''
    
    categories = Category.objects.filter(user=request.user)
    return render(
        request,
        'tasks/category_list.html',
        {'categories': categories}
    )


def create_category(request):
    '''
    
    '''
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(
        request,
        'tasks/category_form.html',
        {'form': form}
        )
    
def edit_category(request, category_id):
    '''
    
    '''
    
    category = Category.objects.get(id=category_id, user=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(
        request,
        'tasks/category_form.html',
        {'form': form}
        )

def delete_category(request, category_id):
    '''
    
    '''
    
    category = Category.objects.get(id=category_id, user=request.user)
    category.delete()
    return redirect('category_list')

def task_list(request):
    '''
    View function that displays list of tasks associated with current logged user.
    Retrieves all tasks associated with logged user from database and renders template
    to display the tasks.
    '''
    
    tasks = Task.objects.filter(user=request.user)
    return render(
        request,
        'tasks/task_list.html',
        {'tasks': tasks}
        )

def create_task(request):
    '''
    Handles creation of a new task working alongside a form.
    Works with both rendering form to create a new task (GET requests)
    and process submitted form data creating a new task (POST requests),
    if form submission is successful, user is redirected to task_list view.
    '''
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(
        request,
        'tasks/task_form.html',
        {'form': form}
        )

def edit_task(request, task_id):
    '''
    Handles the editing of an existing task.
    Handles both rendering of form to edit an existing task (GET requests) and
    process of the submitted form data to update a task (POST requests. If form
    submission is successful user is redirected to task_list view.
    '''
    
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(
        request,
        'tasks/task_form.html',
        {'form': form}
        )

def delete_task(request, task_id):
    '''
    Handles deletion of existing task.
    Deletes a task based on its ID and current logged-in user,
    after deletion it redirects user to task_list views displaying
    updated list od all tasks.
    '''
    
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')
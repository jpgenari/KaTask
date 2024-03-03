from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import TaskForm, CategoryForm

# Create your views here.

def landing_page(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    return render(request, 'tasks/landing_page.html')

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
        form = TaskForm(request.POST, request.FILES)
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
    
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(
        request,
        'tasks/task_form.html',
        {'form': form}
        )

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

def undo_complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = False
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    '''
    Handles deletion of existing task.
    Deletes a task based on its ID and current logged-in user,
    after deletion it redirects user to task_list views displaying
    updated list od all tasks.
    '''
    
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def category_list(request):
    '''
    '''
    
    categories = Category.objects.filter(user=request.user)
    return render(
        request,
        'tasks/category_list.html',
        {'categories': categories}
    )

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    tasks = Task.objects.filter(category=category)
    task_count = tasks.count()
    
    return render(
        request,
        'tasks/category_detail.html',
        {
            'category': category,
            'tasks': tasks,
            'task_count': task_count
            }
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
    
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
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
    
    category = Category.objects.get(id=category_id)
    
    category.delete()
    return redirect('category_list')

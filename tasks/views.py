from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from django.utils import timezone
from django.db.models import Count
from .models import Task, Category
from .forms import TaskForm, CategoryForm

# Create your views here.


def display_tasks(request):
    '''
    Uses method .date() to pass date without HH:MM to run
    taks expired feature on front end.
    Displays list of tasks associated with logged-in user.
    Gets all tasks associated with logged-in user and renders
    template displaying all tasks.
    If user not logged-in, redirects user to home.html.
    '''

    now = timezone.now()
    now_date_only = now.date()

    if not request.user.is_authenticated:
        return redirect('home')

    tasks = Task.objects.filter(user=request.user)

    return render(
        request,
        'tasks/task.html',
        {
            'tasks': tasks,
            'now': now_date_only,
        }
    )


def create_task(request):
    '''
    Creates new tasks alongside TaskForm. Renders form to
    create new task (GET) and process submitted form with
    data to create task (POST). After submission, redirects
    to task.
    '''

    if request.method == 'POST':
        form = TaskForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.add_message(request, messages.SUCCESS, 'Task Created!')
            return redirect('tasks')
    else:
        form = TaskForm(user=request.user)

    return render(
        request,
        'tasks/task_form.html',
        {'form': form}
        )


def edit_task(request, task_id):
    '''
    Edits current tasks working with TaskForm. Checks if object exists and
    if logged-in user is owner of task (to prevent error when user enters
    object ID manually on url) displaying alert messages and redirecting to
    task.
    Then renders TaskForm (GET) and process submitted form data to update
    task in DB (POST). After submission, redirects to tasks.html.
    '''

    try:
        task = get_object_or_404(Task, id=task_id)
    except Http404:
        messages.add_message(
            request, messages.ERROR, "This task does not exist.")
        return redirect('tasks')

    if task.user != request.user:
        messages.add_message
        (request, messages.ERROR, "This task does not exist.")
        return redirect('tasks')

    elif request.method == 'POST':
        form = TaskForm(
            request.user, request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.add_message(request, messages.SUCCESS, 'Task Updated!')
            return redirect('tasks')
    else:
        form = TaskForm(user=request.user, instance=task)

    return render(
        request,
        'tasks/task_form.html',
        {'form': form}
        )


def complete_task(request, task_id):
    '''
    Marks task as 'Complete' by user. Gets task ID, confirm user,
    changes its complete field to True and saves on DB. Then
    redirects to tasks.html.
    '''

    task = Task.objects.get(id=task_id)

    if task.user == request.user:
        task.completed = True
        task.save()
        messages.add_message(
            request, messages.SUCCESS, 'Task completed, moved down!')

    return redirect('tasks')


def undo_complete_task(request, task_id):
    '''
    Marks task as 'Uncomplete' (undo complete) by user. Gets task ID,
    confirm user, changes its complete field to False and saves on DB.
    Then redirects to tasks.html.
    '''

    task = Task.objects.get(id=task_id)

    if task.user == request.user:
        task.completed = False
        task.save()
        messages.add_message(
            request, messages.SUCCESS, 'Task back to your list!')

    return redirect('tasks')


def delete_task(request, task_id):
    '''
    Deletes existing task. Gets task ID, deletes it from
    DB and redirects to tasks.html.
    '''

    task = Task.objects.get(id=task_id)

    if task.user == request.user:
        task.delete()
        messages.add_message(request, messages.SUCCESS, 'Task Deleted!')

    return redirect('tasks')


def display_categories(request):
    '''
    Displays list of categories associated with logged-in user.
    Gets all categories associated with logged-in user and renders
    template displaying all categories.
    '''

    if not request.user.is_authenticated:
        messages.add_message(
            request, messages.ERROR, 'Login first to view your Categories')
        return redirect('home')

    categories = Category.objects.filter(user=request.user).annotate(
        task_count=Count('task')).order_by('category_name')

    return render(
        request,
        'tasks/category.html',
        {
            'categories': categories,
        }
    )


def category_detail(request, category_id):
    '''
    Uses method .date() to pass date without HH:MM to run
    taks expired feature on front end.
    Displays details of a category associated with logged-in user.
    Checks if category ID and associated tasks exists and if they
    belong to logged-in user (to prevent error when user enters category
    object ID manually on url) displaying alert message and redirecting to
    category-list.
    Then renders category_detail template with associated tasks.
    '''

    now = timezone.now()
    now_date_only = now.date()

    try:
        category = get_object_or_404(Category, id=category_id)
        tasks = Task.objects.filter(category=category)
        task_count = tasks.count()
    except Http404:
        return redirect('categories')

    if category.user != request.user:
        messages.add_message(
            request, messages.ERROR, "This category does not exist.")
        return redirect('categories')

    return render(
        request,
        'tasks/category_detail.html',
        {
            'category': category,
            'tasks': tasks,
            'task_count': task_count,
            'now': now_date_only,
            }
        )


def create_category(request):
    '''
    Creates new categories alongside CategoryForm. Renders form to
    create new category (GET) and process submitted form with
    data to create category (POST). After submission, redirects
    to display_categories.
    '''

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.add_message(
                request, messages.SUCCESS, 'Category Created!')
            return redirect('categories')
    else:
        form = CategoryForm()

    return render(
        request,
        'tasks/category_form.html',
        {'form': form}
        )


def edit_category(request, category_id):
    '''
    Edits current categories working with CategoryForm. Checks if object
    exists and if logged-in user is owner of category (to prevent error when
    user enters object ID manually on url) displaying alert messages and
    redirects to display_categories.
    Then renders CategoryForm (GET) and process submitted form data to update
    category in DB (POST). After submission, redirects to display_categories.
    '''

    try:
        category = get_object_or_404(Category, id=category_id)
    except Http404:
        messages.add_message(
            request, messages.ERROR, "This category does not exist.")
        return redirect('categories')

    if category.user != request.user:
        messages.add_message(
            request, messages.ERROR, "This category does not exist.")
        return redirect('categories')
    elif request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Category Updated!')
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)

    return render(
        request,
        'tasks/category_form.html',
        {'form': form}
        )


def delete_category(request, category_id):
    '''
    Deletes existing category. Gets category ID, deletes it from DB and
    redirects to display_categories.
    '''

    category = Category.objects.get(id=category_id)

    if category.user == request.user:
        category.delete()
        messages.add_message(request, messages.SUCCESS, 'Category Deleted!')

    return redirect('categories')

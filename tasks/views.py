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
    Displays a list of tasks associated with the logged-in user.
    Retrieves tasks for the logged-in user and renders the template
    displaying all tasks.
    **Context:**
    ``tasks``
        A queryset of tasks associated with the logged-in user. Each task is an
        instance of :model:`tasks.Task`.
    ``now``
        The current date without the time component (HH:MM), used for front-end
        tasks expired feature.
    **Template:**
    :template:`tasks/task.html`
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
    Creates a new task using the TaskForm. Renders the form to
    create a new task (GET) and processes the submitted form data
    to create the task (POST). After submission, redirects to the
    tasks page.
    **Context:**
    ``form``
        An instance of :class:`tasks.forms.TaskForm` for creating a new task.
    **Template:**
    :template:`tasks/task_form.html`
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
    Edits an existing task using the TaskForm. Checks if the task exists
    and if the logged-in user is the owner of the task (to prevent errors
    when the user manually enters the object ID in the URL).
    If the task does not exist or the user is not the owner, displays an
    alert message and redirects to the tasks page.
    Then renders the TaskForm (GET) and processes submitted form data to
    update the task in the database (POST). After submission, redirects to
    the tasks page.
    **Parameters:**
    ``task_id``
        The ID of the task to be edited.
    **Context:**
    ``form``
        An instance of :class:`tasks.forms.TaskForm` for editing the task.
    **Template:**
    :template:`tasks/task_form.html`
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
    Marks a task as 'Complete' by the user. Retrieves the task with the given
    ID, confirms that the user is the owner of the task, sets its `completed`
    field to True, and saves it in the database.
    **Parameters:**
    ``task_id``
        The ID of the task to be marked as complete.
    **Context:**
    ``task``
        The task instance with the given ID, marked as complete.
    **Template:**
    :template:`tasks/task.html`
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
    Marks a task as 'Uncomplete' (undo complete) by the user. Retrieves the
    task with the given ID, confirms that the user is the owner of the task,
    sets its `completed` field to False, and saves it in the database.
    **Parameters:**
    ``task_id``
        The ID of the task to be marked as uncomplete.
    **Context:**
    ``task``
        The task instance with the given ID, marked as uncomplete.
    **Template:**
    :template:`tasks/task.html`
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
    Deletes an existing task. Retrieves the task with the given ID,
    confirms that the user is the owner of the task, deletes it from
    the database, and redirects to the tasks page.
    **Parameters:**
    ``task_id``
        The ID of the task to be deleted.
    **Context:**
    None.
    **Template:**
    :template:`tasks/task.html`
    '''

    task = Task.objects.get(id=task_id)

    if task.user == request.user:
        task.delete()
        messages.add_message(request, messages.SUCCESS, 'Task Deleted!')

    return redirect('tasks')


def display_categories(request):
    '''
    Displays a list of categories associated with the logged-in user.
    Retrieves all categories associated with the logged-in user, including
    the count of tasks for each category, and renders the template displaying
    all categories.
    **Context:**
    ``categories``
        A queryset of categories associated with the logged-in user.
        Each category includes an additional field ``task_count`` representing
        the count of tasks for that category.
    **Template:**
    :template:`tasks/category.html`
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
    tasks expired feature on the front end.
    Displays details of a category associated with the logged-in user.
    Checks if the category ID and associated tasks exist and if they
    belong to the logged-in user (to prevent an error when the user enters
    the category object ID manually in the URL), displaying an alert message
    and redirecting to the category list.
    Then renders the category_detail template with associated tasks.
    **Parameters:**
    ``category_id``
        The ID of the category to be displayed in detail.
    **Context:**
    ``category``
        The category instance with the given ID.
    ``tasks``
        A queryset of tasks associated with the specified category.
    ``task_count``
        The count of tasks associated with the specified category.
    ``now``
        The current date without the time component (HH:MM), used for the
        front-end tasks expired feature.
    **Template:**
    :template:`tasks/category_detail.html`
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
    Creates new categories alongside the CategoryForm. Renders the form to
    create a new category (GET) and processes the submitted form with
    data to create a category (POST). After submission, redirects
    to display_categories.
    **Context:**
    ``form``
        An instance of :class:`tasks.forms.CategoryForm` for creating a new
        category.
    **Redirects:**
    :url:`categories`
    **Template:**
    :template:`tasks/category_form.html`
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
    Edits current categories working with the CategoryForm. Checks if the
    object exists and if the logged-in user is the owner of the category (to
    prevent an error when the user enters the object ID manually in the URL),
    displaying alert messages and redirecting to display_categories.
    Then renders the CategoryForm (GET) and processes submitted form data to
    update the category in the database (POST). After submission, redirects to
    display_categories.
    **Parameters:**
    ``category_id``
        The ID of the category to be edited.
    **Context:**
    ``form``
        An instance of :class:`tasks.forms.CategoryForm` for editing the
        category.
    **Template:**
    :template:`tasks/category_form.html`
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
    Deletes an existing category. Retrieves the category with the given ID,
    confirms that the user is the owner of the category, deletes it from
    the database, and redirects to display_categories.
    **Parameters:**
    ``category_id``
        The ID of the category to be deleted.
    **Template:**
    :template:`tasks/category.html`
    '''

    category = Category.objects.get(id=category_id)

    if category.user == request.user:
        category.delete()
        messages.add_message(request, messages.SUCCESS, 'Category Deleted!')

    return redirect('categories')

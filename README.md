# KaTask

KaTask is an online task management app, focused in minimalism UI. Its name comes from Japanese *'Ka' - or '化' -* which means transforming or making something into plus, task. Here, users will only focus on the tasks themselves, with no distractions at all.

## Table of contents

## UX

## Steps taken

1. Create repository;
2. Install Django package;

    ```pip3 install Django~=4.2.1```
3. Create and add requirements to requirements doc;
    ```pip3 freeze --local > requirements.txt````
4. Create Django project;

    ```django-admin startproject katask .```
5. Create a Django app inside the project;

    ```python3 manage.py startapp tasks```
6. Create views in tasks/views.py (Example from [CI Django Project](https://github.com/jpgenari/CI-django_project?tab=readme-ov-file#creating-views]));
7. Add app in [settings.py](https://github.com/jpgenari/CI-django_project?tab=readme-ov-file#creating-views);
8. Deploy to [Heroku](https://github.com/jpgenari/CI-django_project?tab=readme-ov-file#deploying-to-heroku);
9. Create the database with PostgreSWL - in this case using [ElephantSQL.com](https://code-institute-students.github.io/deployment-docs/02-elephantsql/elephantsql-01-sign-up) and connect to the code;
10. Connect DataBase to Heroku and deploy;
11. Create model code to handle data;
12. Create and make migrations;
13. Build homepage with Django generic views;
    
    A. Create **url.py** inside tasks directory;
    
    B. Update **katask/urls.py**;

    C. Create a **templates** directory in the **tasks** app with another directory nested inside, named 'tasks';

    D. Create a **tasks_list.htmnl** file and add HTML to it;


Fixed bug where users were able to view all categories when creating a task: https://copyprogramming.com/howto/django-forms-filter-field-by-user-id-3
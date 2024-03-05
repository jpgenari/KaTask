# KaTask | Manager

KaTask | Manager is an online task management app, featuring a minimalist UI. Its name is inspired by the Japanese word 'Ka' (化), which translates to transforming or making something better—pairing perfectly with 'task.' In this app, users can solely concentrate on their tasks without any distractions.

Link to the live web app: [Ka | Task](https://katask-9e69d33c7144.herokuapp.com/)

![Responsive Mockup]()
View it on [Am I responsive?](https://ui.dev/amiresponsive?url=https://katask-9e69d33c7144.herokuapp.com/)

## Table of contents

+ [UX](#ux "UX")
  + [UI](#ui "UI")
  + [FlowChart](#flowchart "FlowChart")
  + [Landing page](#landing-page "Landing page")
  + [Welcome & view instructions](#welcome--view-instructions "Welcome & view instructions")
  + [Instructions](#instructions "Instructions")
  + [Game level](#game-level "Game level")
  + [Guessing the number](#guessing-the-number "Guessing the number")
  + [Ending the game](#ending-the-game "Ending the game")
  + [Displaying results](#displaying-results "Displaying results")
  + [Features Left to Implement or Future Features](#features-left-to-implement-or-future-features "Features Left to Implement or Future Features")
+ [USER STORIES](#user-stories "USER STORIES")
+ [DATA SCHEMA](#data-schema "DATA SCHEMA")
+ [VALIDATING AND TESTING](#validating-and-testing "VALIDATING AND TESTING")
  + [Validator](#validator "Validator")
  + [Testing as a Table](#testing-as-a-table "Testing as a Table")
+ [BUGS](#bugs "BUGS")
  + [Solved bugs](#solved-bugs "Solved bugs")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [TOOLS AND TECHNOLOGIES](#tools-and-technologies "TOOLS AND TECHNOLOGIES")
  + [Languages](#languages "Languages")
  + [Python Libraries and Modules](#python-libraries-and-modules "Python Libraries and Modules")
  + [Tools](#tools "Tools")
  + [Database](#database "Database")
+ [DEVELOPMENT AND DEPLOYMENT](#development-and-deployment "DEVELOPMENT AND DEPLOYMENT")
  + [Local](#local "Local")
  + [Google Sheets with Python](#google-sheets-with-python "Google Sheets with Python")
  + [Heroku](#heroku "Heroku")
+ [CREDITS](#credits "CREDITS")
  + [Content](#content "Content")
  + [Acknowledgement](#acknowledgement "Acknowledgement")

## UX

### UI

KaTask | Manager aims to transform your traditional task notebook into a digital format. We won't inundate you with distracting alerts. Instead, we encourage you to check your daily tasks in our minimalist user interface and then get them done—keeping it simple and focused.

### FlowChart

The flowchart has proven to be an invaluable tool for strategic planning, providing insightful guidance into the construction of the application by mapping out every step taken by users. This detailed chart was crafted using [Draw.io](https://www.drawio.com/).

  ![FlowChart](/docs/readme_images/katask.drawio.png)

### Landing page





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

Reference: https://medium.com/@sarahisdevs/creating-a-task-manager-to-do-list-application-using-python-django-1afe8b33df65
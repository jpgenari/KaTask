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
  + [Login & Register](#login-and-register "Login & Register")
  + [Tasks](#tasks "Tasks")
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

#### Landing Page: Version 1 - Welcome and Registration

  Upon your initial visit or when not logged in, Version 1 of our landing page welcomes you with a dynamic interface. The app's name takes center stage at the top, accompanied by a menu presenting options such as 'Register' and 'Login.' To encourage interaction, a prominent 'Get Started' button directs users seamlessly to the login process. The page then unfolds with key features, a user-friendly guide, feedback from users, and a persistent footer offering insights into the app's nature and links to our social media presence. The header, menu, and footer remain visible at all times, ensuring a seamless user experience.
  
  ![Landingv1](/docs/readme_images/landing-page-v1.png)

#### Landing Page: Version 2 - Personalized and Task-Centric

  For users already logged in, Version 2 of our landing page provides a tailored experience. The app's name and a menu featuring 'Home,' 'Tasks,' 'Categories,' and 'Logout' greet users. A personalized message beneath the menu confirms their logged-in status, displaying the username. Clicking on the header takes users directly to their tasks—the heart of the app—while the 'Home' option stays accessible for checking instructions or navigating back to the main page. This version ensures efficiency for users immersed in the app's functionalities. As always, the header, menu, and footer remain fixed for easy navigation.
  
  ![Landingv1](/docs/readme_images/landing-page-v2.png)

These two versions cater to different stages of user interaction, offering a seamless transition from exploration to engagement based on the user's status within the app.

### Login & Register

#### Login Page: Swift Access to Your Tasks

  The Login Page invites users, prompting them to log in for task access. New users are encouraged to sign up first. Login requires a username and password, ensuring a secure and simple entry.
  
  ![Login](/docs/readme_images/sign-in.png)

#### Register Page: Effortless KaTask Onboarding

  The Register Page also welcomes new users, suggesting login for existing accounts. For registration, users provide a username, optional email, and a secure password, guided by clear instructions.

  ![Login](/docs/readme_images/sign-up.png)

After successful registration, users are directed to the Version 2 Home Page. A modal message accompanies this, confirming their successful sign-in.

  ![Login](/docs/readme_images/sign-in-success.png)

### Tasks



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
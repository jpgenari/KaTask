# KaTask | Manager

KaTask | Manager is an online task management app, featuring a minimalist UI. Its name is inspired by the Japanese word 'Ka' (化), which translates to transforming or making something better—pairing perfectly with 'task.' In this app, users can solely concentrate on their tasks without any distractions.

Link to the live web app: [Ka | Task](https://katask-9e69d33c7144.herokuapp.com/)

![Responsive Mockup]()
View it on [Am I responsive?](https://ui.dev/amiresponsive?url=https://katask-9e69d33c7144.herokuapp.com/)

## Table of contents

+ [UX](#ux "UX")
  + [UI](#ui "UI")
  + [FlowChart](#flowchart "FlowChart")
  + [Features](#features "Features")
    - [Landing page](#landing-page "Landing page")
    - [Login & Register](#login-and-register "Login & Register")
    - [Tasks](#tasks "Tasks")
    - [New Task](#new-task "New Task")
    - [Categories](#categories "Categories")
    - [Category Details](#category-details "Category Details")
    - [Logout](#logout "Logout")
    - [Admin](#admin "Admin")
    - [Features Left to Implement or Future Features](#features-left-to-implement-or-future-features "Features Left to Implement or Future Features")
+ [USER STORIES](#user-stories "USER STORIES")
+ [ENTITY RELATIONSHIP DIAGRAM](#entity-relationship-diagram "ENTITY RELATIONSHIP DIAGRAM")
+ [VALIDATING AND TESTING](#validating-and-testing "VALIDATING AND TESTING")
  + [Validator](#validator "Validator")
  + [Manual Testing](#manual-testing "Manual Testing")
+ [BUGS](#bugs "BUGS")
  + [Solved Bugs](#solved-bugs "Solved Bugs")
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

### Features

#### Landing page

##### Landing Page: Version 1

Upon your initial visit or when not logged in, Version 1 of our landing page welcomes you with a dynamic interface. The app's name takes center stage at the top, accompanied by a menu presenting options such as 'Register' and 'Login.' To encourage interaction, a prominent 'Get Started' button directs users seamlessly to the login process. The page then unfolds with key features, a user-friendly guide, feedback from users, and a persistent footer offering insights into the app's nature and links to our social media presence. The header, menu, and footer remain visible at all times, ensuring a seamless user experience.
  
  ![Landing-v1](/docs/readme_images/landing-page-v1.png)

##### Landing Page: Version 2

For users already logged in, Version 2 of our landing page provides a tailored experience. The app's name and a menu featuring 'Home,' 'Tasks,' 'Categories,' and 'Logout' greet users. A personalized message beneath the menu confirms their logged-in status, displaying the username. Clicking on the header takes users directly to their tasks—the heart of the app—while the 'Home' option stays accessible for checking instructions or navigating back to the main page. This version ensures efficiency for users immersed in the app's functionalities. As always, the header, menu, and footer remain fixed for easy navigation.

  ![Landing-v2](/docs/readme_images/landing-page-v2.png)

These two versions cater to different stages of user interaction, offering a seamless transition from exploration to engagement based on the user's status within the app.

#### Login & Register

##### Login Page

The Login Page invites users, prompting them to log in for task access. New users are encouraged to sign up first. Login requires a username and password, ensuring a secure and simple entry.
  
  ![Login](/docs/readme_images/sign-in.png)

##### Register Page

The Register Page also welcomes new users, suggesting login for existing accounts. For registration, users provide a username, optional email, and a secure password, guided by clear instructions.

  ![Register](/docs/readme_images/sign-up.png)

After successful registration, users are directed to the Version 2 Home Page. A modal message accompanies this, confirming their successful sign-in.

  ![Logged-in](/docs/readme_images/sign-in-success.png)

#### Tasks

The Tasks Page offers a clean layout for easy task tracking. If no tasks are present, a prompt encourages users to kickstart by adding their first task via the "Add Task" button.

  ![Tasks-1](/docs/readme_images/tasks-1.png)

For existing tasks, each card displays the task name prominently, followed by a concise block with details like description, due date, category, and priority. Tasks are intelligently ordered:

**1. Completion Status**: Uncompleted tasks take precedence, followed by completed tasks (greyed out at the bottom).
  
**2. Due Date:** Tasks are sorted by proximity to their expiry date.
  
**3. Priority:** Higher-priority tasks are highlighted for quick identification.
  
**4. Creation Date:** Older tasks appear first, encouraging the completion of older items before newer ones.

  ![Tasks-2](/docs/readme_images/tasks-2.png)
  
Task cards also feature two buttons:

* **Complete/Undo Complete:** Dynamically adjusts based on task completion status.
* **Delete:** Confirms deletion with a modal prompt, ensuring intentional actions.

Effortless task management with a focus on simplicity and user control, ensuring users can prioritize and organize their tasks efficiently.

  ![Tasks-Delete](/docs/readme_images/task-delete.png)

#### New Task

When clicking on "The New", users are directed to new task form to input task details, including title and description, select a category (with the option to add a new one via the Categories Page), specify a due date, set priority, and save. After saving, users are redirected to the main Tasks Page, ensuring a quick and straightforward task entry process.

  ![New-Task](/docs/readme_images/new-task.png)

#### Categories

The Categories Page mirrors the user-friendly design of the Tasks Page, featuring a "New Category" button to add fresh categories. In the absence of categories, a motivating message prompts users to begin categorizing their tasks.

  ![Categories-1](/docs/readme_images/categories-1.png)

With existing categories, users encounter a neatly organized list in alphabetical order, each displaying the number of tasks assigned. Clicking on a category name directs users to detailed category information (covered in the next section).

  ![Categories-2](/docs/readme_images/categories-2.png)

For added convenience, an "Edit" button allows users to modify category details, while a "Delete" button triggers a modal confirmation message. This ensures intentional actions and informs users that deleting a category does not remove associated tasks; instead, they become uncategorized. This thoughtful design promotes efficient category management while maintaining task integrity.

  ![Category-Delete](/docs/readme_images/category-delete.png)

#### Category Details

Selecting a category opens the Category Details Page, showcasing the number of assigned tasks. Users can swiftly add a new task with the "New Task" button and view the task list for that category. If no tasks are assigned, a message encourages users to add a task, ensuring a proactive approach to task management within the selected category.

  ![Category-Detail-1](/docs/readme_images/category-detail-1.png)

  ![Category-Detail-2](/docs/readme_images/category-detail-2.png)

#### Logout

Clicking logout confirms sign-out and redirects to the home page.

  ![Logout](/docs/readme_images/sign-out.png)

#### Features Left to Implement or Future Features

* **Left to Implement** the option to upload images to tasks. The groundwork has been laid with Cloudinary integration and added to database (models.py), and the feature is on the horizon for enhanced task customization.

* **Future Future** options for users to reset and change passwords. This additional functionality enhances user account security and provides a more comprehensive set of account management features.

* **Future Future** the ability to create categories while adding tasks. This user-friendly feature enhances the task creation process, providing a seamless and efficient experience.

* **Future Future** grant secure task review access through templates, ensuring a smoother user interface and reducing the risk of disruptions. This also facilitates easier access for additional users if needed. At the moment, this is restricted superusers, a shortcut has been added to menu for superusers.

* **Future Future** integrate a user-friendly filtering option into the UI, enabling efficient task searches as more tasks accumulate. This enhancement aims to streamline user navigation and improve the overall user experience.

## USER STORIES AND AGILE

### Admin Management

* As a **Site Admin** I can **create new superusers** so that **other superusers can help managing task manager app**.

* As a **Site Admin** I can **create, read and delete any task from any user** so that **I can guarantee no abuse is made in the task manager**.

* As a **Site Adm** I can **update content on home page with (features, instructions and feedback) though database** so that **I can keep home page updated**.

### User account

* As a **Site User** I can **register an account** so that **view and manage my tasks**.

### Tasks management

* As a **Site User** I can **see instructions and info about the app** so that **I can know how to use the task manager**.

* As a **Site User** I can **view a list of all my tasks** so that **I can see tasks I need to get done**.

* As a **Site User** I can **add, edit, delete or mark as completed task** so that **manage my tasks**.

* As a **Site User** I can **create, edit or remove categories** so that **assign categories to tasks for easier handling**.

### Agile Development

Project launched on GitHub Projects to systematically organize tasks, categorizing them into epics and breaking them into manageable parts. Initially focusing on the backend, I addressed each feature to get the app running on bare minimum. Once the backend was in place, I transitioned to applying and setting up the frontend components. This structured approach aimed to ensure efficient progress. Following the identified needs, I followed the steps from the mock project to implement each feature.

Kanban board available [here](https://github.com/users/jpgenari/projects/6/views/1?layout=board).

## ENTITY RELATIONSHIP DIAGRAM

The Entity Relationship Diagram (ERD) for the Django project's created apps was generated using Graphviz. This visualization specifically represents the relationships and entities within the defined apps, providing a comprehensive overview of the data structure in the project.

  ![ERD](/docs/readme_images/my_project_erd.png)

## VALIDATING AND TESTING

### Validator


### Manual Testing


## BUGS

### Solved Bugs

* Fixed a bug where users could view all categories added by all users when creating a task. The issue has been successfully addressed with the assistance of the information from this [CopyProgramming](https://copyprogramming.com/howto/django-forms-filter-field-by-user-id-3) post.

  Below, code applied in the **tasks/forms.py** inside class **TaskForm()** to fix bug:

  ```python
      def __init__(self, user, *args, **kwargs):
          '''
          Ensures that 'Category' field in TaskForm is populated with categories
          belonging to logged-in user and also allows task without category.
          Parameters:
          - user: The user for whom the form is being initialized.
          - *args, **kwargs: Additional arguments and keyword arguments that can
          be passed to the form.
          '''
          super(TaskForm, self).__init__(*args, **kwargs)
          self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.filter(user=user),  required=False)
    ```

* Successfully addressed a bug in the tasks.html template where a conditional statement wasn't functioning as intended. This resulted in the CSS class not being applied, affecting the background color display for tasks beyond their due date. The issue has been resolved with insights from a mentor, including a fix for a bug that occurred when comparing task due dates in DD/MM/YYYY format with the current date, which includes HH:MM. This was fixed by applying string manipulation in views to strip the hour and minute before passing the date to the conditional. The solution now utilizes the **now.date()** method to ensure accurate task date comparisons.

  Below, code applied in the **task_details.html** and to function **display_tasks()** to fix bug:

    ```python
        def display_tasks(request):
            '''
            Displays list of tasks associated with logged-in user.
            Gets all tasks associated with logged-in user and renders 
            template displaying all tasks.
            now.date() removes HH:MM before passing 'now' to conditional.
            '''
            
            now = timezone.now()
            now_date_only = now.date()
            
            tasks = Task.objects.filter(user=request.user)
            return render(
                request,
                'tasks/task.html',
                {
                    'tasks': tasks,
                    'now': now_date_only,
                }
            )
    ```

    ```
      <li class="list-group-item {% if not task.completed and task.due_at < now %}task-expired{% elif task.completed %}completed-task{% endif %}">
    ```

### Unfixed Bugs

There are no unfixed bugs.






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
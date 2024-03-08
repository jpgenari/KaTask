# KaTask | Manager

KaTask | Manager is an online task management app, featuring a minimalist UI. Its name is inspired by the Japanese word 'Ka' (化), which translates to transforming or making something better—pairing perfectly with 'task.' In this app, users can solely concentrate on their tasks without any distractions.

Link to the live web app: [Ka | Task](https://katask-9e69d33c7144.herokuapp.com/)

![Responsive Mockup from am I responsive screenshot](/docs/readme_images/am-i-responsive.png)
View it on [Am I responsive?](https://ui.dev/amiresponsive?url=https://katask-9e69d33c7144.herokuapp.com/)

## Table of contents

+ [UX](#ux "UX")
  + [UI](#ui "UI")
  + [Wireframes](#wireframes "Wireframes")
  + [Colors](#colors "Colors")
  + [FlowChart](#flowchart "FlowChart")
  + [Features](#features "Features")
    - [Landing page](#landing-page "Landing page")
    - [Login & Register](#login--register "Login & Register")
    - [Tasks](#tasks "Tasks")
    - [New Task](#new-task "New Task")
    - [Categories](#categories "Categories")
    - [Category Details](#category-details "Category Details")
    - [Logout](#logout "Logout")
    - [Features Left to Implement or Future Features](#features-left-to-implement-or-future-features "Features Left to Implement or Future Features")
+ [USER STORIES AND AGILE](#stories-and-agile "USER STORIES AND AGILE")
  + [User Stories](#user-stories "User Stories")
    - [Admin Management](#admin-management "Admin Management")
    - [User account](#user-account "User account")
    - [Tasks management](#tasks-management "Tasks management")
  + [Agile Development](#dgile-development, "Agile Development")
+ [ENTITY RELATIONSHIP DIAGRAM](#entity-relationship-diagram "ENTITY RELATIONSHIP DIAGRAM")
+ [VALIDATING AND TESTING](#validating-and-testing "VALIDATING AND TESTING")
  + [Validator](#validator "Validator")
    - [HTML - W3C Validator](#html--w3c-validator "HTML - W3C Validator")
    - [CSS - Jigsaw W3C Validator](css---jigsaw-w3c-validator "CSS - Jigsaw W3C Validator")
    - [JavaScript - JS Hint](#javascript-js-hint "JavaScript - JS Hint")
    - [Python and Django - CI Python Linter](#python-and-django---ci-python-linter "Python and Django - CI Python Linter")
    - [Performance - Google Lighthouse](#performance---google-lighthouse "Performance - Google Lighthouse")
  + [Manual Testing](#manual-testing "Manual Testing")
+ [BUGS](#bugs "BUGS")
  + [Solved Bugs](#solved-bugs "Solved Bugs")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [TECHNOLOGIES](#technologies "TECHNOLOGIES")
+ [DEPLOYMENT](#Deployment "DEPLOYMENT")
  + [ElephantSQL Database](#elephantsql-database "ElephantSQL Database")
  + [Cloudinary API](#cloudinary-api "Cloudinary API")
  + [Heroku Deployment](#heroku-deployment "Heroku Deployment")
  + [Local Deployment](#local-deployment "Local Deployment")
  + [Cloning](#cloning "Cloning")
  + [Forking](#forking "Forking")
+ [CREDITS](#credits "CREDITS")
  + [Content](#content "Content")
  + [Acknowledgement](#acknowledgement "Acknowledgement")

## UX

### UI

KaTask | Manager aims to transform your traditional task notebook into a digital format. We won't inundate you with distracting alerts. Instead, we encourage you to check your daily tasks in our minimalist user interface and then get them done—keeping it simple and focused.

### Wireframes

The project wireframes were drawn by hand, emphasizing a minimalist design for a task management notebook. This analog approach ensures a seamless user experience, with each element crafted for efficiency. As the foundational blueprint, these hand-drawn sketches uniquely blend traditional craftsmanship with modern design principles, promising a user-friendly and aesthetically refined final product.

### Colors

The focus of the color scheme is to achieve a minimalist design with high contrast, ensuring the application's accessibility. The color FF6633 has been shaded in order to not break layout harmony, it is used ro display expired tasks, in a subtle way - minimalist.

  ![color scheme screenshot](/docs/readme_images/colors.png)

### FlowChart

The flowchart has proven to be an invaluable tool for strategic planning, providing insightful guidance into the construction of the application by mapping out every step taken by users. This detailed chart was crafted using [Draw.io](https://www.drawio.com/).

  ![flowchart screenshot](/docs/readme_images/katask.drawio.png)

### Features

#### Landing page

##### Landing Page: Version 1

Upon your initial visit or when not logged in, Version 1 of our landing page welcomes you with a dynamic interface. The app's name takes center stage at the top, accompanied by a menu presenting options such as 'Register' and 'Login.' To encourage interaction, a prominent 'Get Started' button directs users seamlessly to the login process. The page then unfolds with key features, a user-friendly guide, feedback from users, and a persistent footer offering insights into the app's nature and links to our social media presence. The header, menu, and footer remain visible at all times, ensuring a seamless user experience.
  
  ![landing page version 1 user not authenticated screenshot](/docs/readme_images/landing-page-v1.png)

##### Landing Page: Version 2

For users already logged in, Version 2 of our landing page provides a tailored experience. The app's name and a menu featuring 'Home,' 'Tasks,' 'Categories,' and 'Logout' greet users. A personalized message beneath the menu confirms their logged-in status, displaying the username. Clicking on the header takes users directly to their tasks—the heart of the app—while the 'Home' option stays accessible for checking instructions or navigating back to the main page. This version ensures efficiency for users immersed in the app's functionalities. As always, the header, menu, and footer remain fixed for easy navigation.

  ![landing page version 2 user authenticated screenshot](/docs/readme_images/landing-page-v2.png)

These two versions cater to different stages of user interaction, offering a seamless transition from exploration to engagement based on the user's status within the app.

#### Login & Register

##### Login Page

The Login Page invites users, prompting them to log in for task access. New users are encouraged to sign up first. Login requires a username and password, ensuring a secure and simple entry.
  
  ![login page sceenshot](/docs/readme_images/sign-in.png)

##### Register Page

The Register Page also welcomes new users, suggesting login for existing accounts. For registration, users provide a username, optional email, and a secure password, guided by clear instructions.

  ![register page screenshot](/docs/readme_images/sign-up.png)

After successful registration, users are directed to the Version 2 Home Page. A modal message accompanies this, confirming their successful sign-in.

  ![screenshot showing success message after login](/docs/readme_images/sign-in-success.png)

#### Tasks

The Tasks Page offers a clean layout for easy task tracking. If no tasks are present, a prompt encourages users to kickstart by adding their first task via the "Add Task" button.

  ![screenshot of tasks section empty](/docs/readme_images/tasks-1.png)

For existing tasks, each card displays the task name prominently, followed by a concise block with details like description, due date, category, and priority. Tasks are intelligently ordered:

**1. Completion Status**: Uncompleted tasks take precedence, followed by completed tasks (greyed out at the bottom).
  
**2. Due Date:** Tasks are sorted by proximity to their expiry date.
  
**3. Priority:** Higher-priority tasks are highlighted for quick identification.
  
**4. Creation Date:** Older tasks appear first, encouraging the completion of older items before newer ones.

  ![screenshot of tasks section populated](/docs/readme_images/tasks-2.png)
  
Task cards also feature two buttons:

* **Complete/Undo Complete:** Dynamically adjusts based on task completion status.
* **Delete:** Confirms deletion with a modal prompt, ensuring intentional actions.

Effortless task management with a focus on simplicity and user control, ensuring users can prioritize and organize their tasks efficiently.

  ![screenshot of delete modal](/docs/readme_images/task-delete.png)

#### New Task

When clicking on "The New", users are directed to new task form to input task details, including title and description, select a category (with the option to add a new one via the Categories Page), specify a due date, set priority, and save. After saving, users are redirected to the main Tasks Page, ensuring a quick and straightforward task entry process.

  ![screenshot of new task form](/docs/readme_images/new-task.png)

#### Categories

The Categories Page mirrors the user-friendly design of the Tasks Page, featuring a "New Category" button to add fresh categories. In the absence of categories, a motivating message prompts users to begin categorizing their tasks.

  ![empty categories page screenshot](/docs/readme_images/categories-1.png)

With existing categories, users encounter a neatly organized list in alphabetical order, each displaying the number of tasks assigned. Clicking on a category name directs users to detailed category information (covered in the next section).

  ![filled with categories page screenshot](/docs/readme_images/categories-2.png)

For added convenience, an "Edit" button allows users to modify category details, while a "Delete" button triggers a modal confirmation message. This ensures intentional actions and informs users that deleting a category does not remove associated tasks; instead, they become uncategorized. This thoughtful design promotes efficient category management while maintaining task integrity.

  ![screenshot of delete modal](/docs/readme_images/category-delete.png)

#### Category Details

Selecting a category opens the Category Details Page, showcasing the number of assigned tasks. Users can swiftly add a new task with the "New Task" button and view the task list for that category. If no tasks are assigned, a message encourages users to add a task, ensuring a proactive approach to task management within the selected category.

  ![empty category details page screenshot](/docs/readme_images/category-detail-1.png)

  ![category details page with tasks assigned screenshot](/docs/readme_images/category-detail-2.png)

#### Logout

Clicking logout confirms sign-out and redirects to the home page.

  ![sign out page screenshot](/docs/readme_images/sign-out.png)

#### Features Left to Implement or Future Features

* **Left to Implement** the option to upload images to tasks. The groundwork has been laid with Cloudinary integration and added to database (models.py), and the feature is on the horizon for enhanced task customization.

* **Future Future** options for users to reset and change passwords. This additional functionality enhances user account security and provides a more comprehensive set of account management features.

* **Future Future** the ability to create categories while adding tasks. This user-friendly feature enhances the task creation process, providing a seamless and efficient experience.

* **Future Future** grant secure task review access through templates, ensuring a smoother user interface and reducing the risk of disruptions. This also facilitates easier access for additional users if needed. At the moment, this is restricted superusers, a shortcut has been added to menu for superusers.

* **Future Future** integrate a user-friendly filtering option into the UI, enabling efficient task searches as more tasks accumulate. This enhancement aims to streamline user navigation and improve the overall user experience.

[Back to top](#katask--manager "Back to top")

## USER STORIES AND AGILE

### User Stories

#### Admin Management

* As a **Site Admin** I can **create new superusers** so that **other superusers can help managing task manager app**.

* As a **Site Admin** I can **create, read and delete any task from any user** so that **I can guarantee no abuse is made in the task manager**.

* As a **Site Adm** I can **update content on home page with (features, instructions and feedback) though database** so that **I can keep home page updated**.

#### User account

* As a **Site User** I can **register an account** so that **view and manage my tasks**.

#### Tasks management

* As a **Site User** I can **see instructions and info about the app** so that **I can know how to use the task manager**.

* As a **Site User** I can **view a list of all my tasks** so that **I can see tasks I need to get done**.

* As a **Site User** I can **add, edit, delete or mark as completed task** so that **manage my tasks**.

* As a **Site User** I can **create, edit or remove categories** so that **assign categories to tasks for easier handling**.

### Agile Development

Project launched on GitHub Projects to systematically organize tasks, categorizing them into epics and breaking them into manageable parts. Initially focusing on the backend, I addressed each feature to get the app running on bare minimum. Once the backend was in place, I transitioned to applying and setting up the frontend components. This structured approach aimed to ensure efficient progress. Following the identified needs, I followed the steps from the mock project to implement each feature.

Kanban board available [here](https://github.com/users/jpgenari/projects/6/views/1?layout=board).

[Back to top](#katask--manager "Back to top")

## ENTITY RELATIONSHIP DIAGRAM

The Entity Relationship Diagram (ERD) for the Django project's created apps was generated using Graphviz. This visualization specifically represents the relationships and entities within the defined apps, providing a comprehensive overview of the data structure in the project.

  ![entity relationship diagram screenshot generated by Graphviz](/docs/readme_images/my_project_erd.png)

[Back to top](#katask--manager "Back to top")

## VALIDATING AND TESTING

### Validator

#### HTML - W3C Validator

No errors flagged by [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fkatask-9e69d33c7144.herokuapp.com%2Fhome).

Usually tests are performed by entering the application url to [W3C Markup Validation Service](https://validator.w3.org/). However, with Django there's a lot of syntax that doesn't play well with the HTML Validator. Also, it is not possible to validate by address (url) as the built app features are only available upon user being logged-in. In order to validate this project's HTML, the following steps were taken.

  - Go to deployed pages after authentication;
  - Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac);
  - This will display the entire compiled code in the browser;
  - Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) - or text input - method;
  - Repeat process for every page that requires a user to be logged-in/authenticated.

**PAGE**|**INPUT**|**SCREENSHOT**
----------|----------|----------
Home Page|[address](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fkatask-9e69d33c7144.herokuapp.com%2Fhome)|![home page validation screenshot](/docs/readme_images/w3c-url.png)
Home Page (Authenticated)|text input|![home page user authenticated validation screenshot](/docs/readme_images/w3c-home.png)
Tasks Page|text input|![tasks page validation screenshot](/docs/readme_images/w3c-tasks.png)
New Task Page|text input|![new task page validation screenshot](/docs/readme_images/w3c-tasks-form.png)
Categories Page|text input|![categories page validation screenshot](/docs/readme_images/w3c-category.png)
Category Details Page|text input|![category details validation screenshot](/docs/readme_images/w3c-category-details.png)
Create Category Page|text input|![create category validation screenshot](/docs/readme_images/w3c-category-form.png)

#### CSS - Jigsaw W3C Validator

No errors flagged on [Jigsaw W3C](https://jigsaw.w3.org/css-validator/)
![jigsaw css validation screenshot](/docs/readme_images/css-test.png)

#### JavaScript - JS Hint

No errors flagged on [JS Hint](https://jshint.com/)
![js hint javascript validation screenshot](/docs/readme_images/jshint.png)

  - The absence of an explicit definition for the bootstrap variable is not an issue because Bootstrap is imported directly in the HTML.
  - There are ten warnings highlight the use of ES6 features like 'const,' 'let,' 'for of,' 'arrow functions,' and 'template literals.' which are not critical issues but reminders to set your ESLint configuration to ES6 ('esversion: 6').

#### Python and Django - CI Python Linter

No errors flagged on [CI Python Linter](https://pep8ci.herokuapp.com/)

**FILE**|**SCREENSHOT**
----------|----------
katask/urls.py|![katask (project) urls.py validation screenshot](/docs/readme_images/plinter-urls.png)
home/admin.py|![home admin.py validation screenshot](/docs/readme_images/plinter-home-admin.png)
home/models.py|![home models.py validation screenshot](/docs/readme_images/plinter-home-models.png)
home/urls.py|![home urls.py validation screenshot](/docs/readme_images/plinter-home-urls.png)
home/views.py|![home views.py validation screenshot](/docs/readme_images/plinter-home-views.png)
tasks/admin.py|![tasks admin.py validation screenshot](/docs/readme_images/plinter-tasks-admin.png)
tasks/forms.py|![tasks forms.py validation screenshot](/docs/readme_images/plinter-tasks-forms.png)
tasks/models.py|![tasks models.py validation screenshot](/docs/readme_images/plinter-tasks-models.png)
tasks/urls.py|![tasks urls.py validation screenshot](/docs/readme_images/plinter-tasks-urls.png)
tasks/views.py|![tasks views.py validation screenshot](/docs/readme_images/plinter-tasks-views.png)

#### Performance - Google Lighthouse

No performance issues flagged when running Google Chrome Lighthouse.

**PAGE URL**|**DEVICE**|**SCREENSHOT**
----------|----------|----------
[Home Page](https://katask-9e69d33c7144.herokuapp.com/home)|Mobile|![home page lighthouse screenshot](/docs/readme_images/lighthouse-home-mobile.png)
[Home Page](https://katask-9e69d33c7144.herokuapp.com/home)|Desktop|![home page lighthouse screenshot](/docs/readme_images/lighthouse-home.png)
[Tasks Page](https://katask-9e69d33c7144.herokuapp.com/)|Mobile|![tasks page lighthouse screenshot](/docs/readme_images/lighthouse-tasks-mobile.png)
[Tasks Page](https://katask-9e69d33c7144.herokuapp.com/)|Desktop|![tasks page lighthouse screenshot](/docs/readme_images/lighthouse-tasks.png)
[New Task Page](https://katask-9e69d33c7144.herokuapp.com/create-task/)|Mobile|![new task page lighthouse screenshot](/docs/readme_images/lighthouse-new-task-mobile.png)
[New Task Page](https://katask-9e69d33c7144.herokuapp.com/create-task/)|Desktop|![new task page lighthouse screenshot](/docs/readme_images/lighthouse-new-task.png)
[Categories Page](https://katask-9e69d33c7144.herokuapp.com/category/)|Mobile|![categories page lighthouse screenshot](/docs/readme_images/lighthouse-categories-mobile.png)
[Categories Page](https://katask-9e69d33c7144.herokuapp.com/category/)|Desktop|![categories page lighthouse screenshot](/docs/readme_images/lighthouse-categories.png)
[New Category Page](https://katask-9e69d33c7144.herokuapp.com/create-category/)|Mobile|![new category page lighthouse screenshot](/docs/readme_images/lighthouse-new-category-mobile.png)
[New Category Page](https://katask-9e69d33c7144.herokuapp.com/create-category/)|Desktop|![new category page lighthouse screenshot](/docs/readme_images/lighthouse-new-category.png)
[Category Details Page](https://katask-9e69d33c7144.herokuapp.com/category/60/)|Mobile|![category details page lighthouse screenshot](/docs/readme_images/lighthouse-category-details-mobile.png)
[Category Details Page](https://katask-9e69d33c7144.herokuapp.com/category/60/)|Desktop|![category details page lighthouse screenshot](/docs/readme_images/lighthouse-category-details.png)
[Signout Page](https://katask-9e69d33c7144.herokuapp.com/accounts/logout/)|Mobile|![signout page lighthouse screenshot](/docs/readme_images/lighthouse-signout-mobile.png)
[Signout Page](https://katask-9e69d33c7144.herokuapp.com/accounts/logout/)|Desktop|![signout page lighthouse screenshot](/docs/readme_images/lighthouse-signout.png)
[Signin Page](https://katask-9e69d33c7144.herokuapp.com/accounts/login/)|Mobile|![signin page lighthouse screenshot](/docs/readme_images/lighthouse-signin-mobile.png)
[Signin Page](https://katask-9e69d33c7144.herokuapp.com/accounts/login/)|Desktop|![signin page lighthouse screenshot](/docs/readme_images/lighthouse-signin.png)
[Signup Page](https://katask-9e69d33c7144.herokuapp.com/accounts/signup/)|Mobile|![signup page lighthouse screenshot](/docs/readme_images/lighthouse-signup-mobile.png)
[Signup Page](https://katask-9e69d33c7144.herokuapp.com/accounts/signup/)|Desktop|![signup page lighthouse screenshot](/docs/readme_images/lighthouse-signup.png)

### Manual Testing

Manual testing following user stories and fully reproducing site user and site admin journey throughout application use. Tests carried over on Google Chrome, Mozilla Firefox, Safari on MacOS system, and mobile testing carried over throughout Google Chrome inspect tool.

**TEST**|**EXPECTED**|**RESULT**
----------|----------|----------
Home|user able to click Register and to sign up page|passed
||user able to click Login and to sign in page|passed
||user able to click 'Get Started' and to sign in page|passed
Register|user able to enter username|passed
||user able to enter email|passed
||user able to enter password|passed
||user able to enter password confirmation|passed
||user able to click 'Sign Up' and confirm registration|passed
Login|user able to enter username|passed
||user able to enter password|passed
||user able to click 'Sign In' and confirm login|passed
Navigation|user able to click 'Home' and go to home page|passed
||user able to click 'Tasks' and go to tasks page|passed
||user able to click 'Categories' and go to categories page|passed
||user able to click 'Logout' and go to logout page|passed
Tasks|user able to view all created tasks|passed
||user able to click 'New Task' and go to new task page|passed
||user able to click on task name, 'DESCRIPTION', 'DUE', 'CATEGORY' and 'PRIORITY' and go to edit task page|passed
||user able to click on 'Complete' and mark task as completed|passed
||user able to click on 'Undo Complete' and mark task as not completed|passed
||user able to click on 'Delete', view deletion confirmation, upon confirmation, task is deleted and return to tasks page and d task as completed|passed
New Task|user able to enter task title|passed
||user able to enter task description|passed
||user able to assign an existing category to the task|passed
||user able to enter due at date for the task|passed
||user able to pick between 'Low', 'Medium' and 'High' priority for the task|passed
||user able to click on 'Save', confirm task creation and return to tasks page|passed
||user able to click on menu items, cancel task creation and go to selected page|passed
Edit Task|user able to update task title|passed
||user able to update task description|passed
||user able to update task category|passed
||user able to update task due at date|passed
||user able to update task priority|passed
||user able to click on 'Save', confirm task update and return to tasks page|passed
||user able to click on menu items, cancel task update and go to selected page|passed
Categories|user able to view all created categories and number os tasks related|passed
||user able to click on 'New Category' and go to new category page|passed
||user able to click on category name and go to category details page|passed
||user able to click on 'Edit' and go to edit category page|passed
||user able to click on 'Delete', view deletion confirmation, upon confirmation, category is deleted and return to tasks page|passed
New Category|user able to enter category name|passed
||user able to click on 'Save', confirm category creation and return to tasks page|passed
||user able to click on menu items, cancel category creation and go to selected page|passed
Edit Category|user able to update category name|passed
||user able to click on 'Save', confirm category update and return to tasks page|passed
||user able to click on menu items, cancel category update and go to selected page|passed
Category Details|user able to view all tasks assigned to the category and manipulate tasks, create new task, edit, mark as complete / undo complete and delete|passed
Logout|user able to click 'Sign Out and logout'|passed
Admin|site admin user able to login to Django Admin Panel|passed
||site admin user able to login to Django Admin Panel and view site administration|passed
||site admin user able to click on 'HOME' and access home administration|passed
||site admin user able to click on 'TASKS' and access tasks administration|passed
Admin Home|site admin user able to add, edit and delete features|passed
||site admin user able to add, edit and delete instructions/how to use|passed
||site admin user able to add, edit and delete user feedback/testimonials to use|passed
Admin Tasks|site admin user able to add, edit and delete any category in the data base|passed
||site admin user able to add, edit and delete any task in the data base|passed

[Back to top](#katask--manager "Back to top")

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

[Back to top](#katask--manager "Back to top")

## TECHNOLOGIES

- [Django](https://www.djangoproject.com/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [Python](https://www.python.org/) is an interpreted, high-level and general-purpose programming language.
- [HTML](https://html.spec.whatwg.org/) is the standard markup language for documents designed to be displayed in a web browser.
- [Cascading Style Sheets (CSS)](https://www.w3.org/Style/CSS/Overview.en.html) is a stylesheet language used to describe the presentation of a document written in HTML or XML.
- [JavaScript](https://www.javascript.com/) is a programming language that adds interactivity to your website.
- [PostgreSQL](https://www.postgresql.org/) is a powerful, open source object-relational database system.
- [Cloudinary](https://cloudinary.com/) is a cloud service that offers a solution to a web application's entire image management pipeline - Cloudinary is installed in the project for future features.
- [Heroku](https://www.heroku.com/) is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

[Back to top](#katask--manager "Back to top")

## DEPLOYMENT

The live deployed application can be found at [https://katask-9e69d33c7144.herokuapp.com/](https://katask-9e69d33c7144.herokuapp.com/), hosted on **Heroku**. Steps to deploy to **Heroku** provided below.

### ElephantSQL Database

The project uses [ElephantSQL](https://www.elephantsql.com) as its PostgreSQL Database provider. Although ElephantSQL previously offered the TinyTurtle plan, it is currently being deprecated. To use it, you'll need to create an account and select this plan; however, the subsequent steps will remain the same.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project, e.g. `stackportfolio`).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project has [Cloudinary API](https://cloudinary.com) installed for online storage of media assets, as Heroku does not persist this type of data. It is currently not in use, reserved for future features

To obtain your Cloudinary API key, create an account and log in.

- For _Primary interest_, you can choose _Programmable Media for image and video API_.
- Optional: _edit your assigned cloud name to something more memorable_.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

- Go to [Heroku](https://heroku.com/) and sign in to the account or create a free an account if necessary.
- From Heroku's dashboard > click on dropdown button "New" and select "Create new app".
- Provide a unique name for your project, and then choose a region closest to you (EU or USA).
- Click on **Create App**"** to proceed.
- Heroku will create the app and take you to the deploy tab.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables:

| Key                     | Value                                                                |
| ----------------------- | -------------------------------------------------------------------- |
| `CLOUDINARY_URL`        | insert your own Cloudinary API key here                              |
| `DATABASE_URL`          | insert your own ElephantSQL database URL here                        |
| `DISABLE_COLLECTSTATIC` | 1 (_this is temporary, and can be removed for the final deployment_) |
| `SECRET_KEY`            | this can be any random secret key         

- Heroku needs two additional files in order to deploy properly(add in your code).

  - requirements.txt
  - Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `web: gunicorn app_name.wsgi > Procfile`
- _replace **app_name** with the name of your primary Django app name; the folder where settings.py is located_. In this case, that is `stackportfolio`.

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

Either:

- Select **Deploy Branch** from the Heroku app when deploying a specific build - **Enable Automatic Deploys" will make Heroku deploy automatically when a new commit is made.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace _app_name_ with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  - `git push heroku main`

### Local Deployment

This project can be cloned or forked in order to make a local copy on your system. For either method, you will need to install any applicable packages found within the _requirements.txt_ file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "insert your Cloudinary API key here")
os.environ.setdefault("DATABASE_URL", "insert your ElephantSQL database URL here")
os.environ.setdefault("SECRET_KEY", "this can be any random secret key")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C`
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

### Cloning

Repository can be cloned by following these steps:

1. Go to the [GitHub repository](https://github.com/stephendawsondev/stackportfolio)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/jpgenari/katask--manager.git`

7. Press Enter to create your local clone.

### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
Repository can be forked by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/stephendawsondev/stackportfolio)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

[Back to top](#katask--manager "Back to top")

## CREDITS

### Content

  - Core App structure and code inspired/taken from [Creating a Task Manager/To-Do List Application using Python Django](https://medium.com/@sarahisdevs/creating-a-task-manager-to-do-list-application-using-python-django-1afe8b33df65) - [Medium](https://medium.com/) subscription required for full reading.
  - App code structure inspired/taken from walkthrough project [Codestar Blog](https://github.com/Code-Institute-Solutions/blog/tree/main), especially Javascript code and modal structure for alerts.
  - READme  structure and content inspired/taken from [Stackportfol.io](Stackportfol.io) and [Rock in Class](https://github.com/Bruna-Andelieri/rock-in-class/blob/main/README.md).
  - [Bootstrap](https://getbootstrap.com/) used for majority of front end - HTML structure and styling.
  - Solution to fix incorrect category filtering when creating tasks found at [Filtering Django Forms Field Based on User ID 3
](https://copyprogramming.com/howto/django-forms-filter-field-by-user-id-3) post.
  - Debugging and refactoring performed with support of [ChatGPT](https://chat.openai.com/).

### Acknowledgement

- A special thanks to my mentor, [Chris Quin](https://github.com/10xOXR), for his outstanding support and patience during the development process. Chris, your encouragement kept me going, and your guidance was crucial to the project's success. I appreciate your unwavering commitment and expertise.

 - A big thank you to my wife, Ana, for her unwavering support and understanding. She, along with Chris, has been instrumental in keeping me motivated and preventing me from giving up, despite the long hours spent coding. Grateful for her constant presence and encouragement.

[Back to top](#katask--manager "Back to top")

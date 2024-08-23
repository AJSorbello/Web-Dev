## Exercise 2.1: Getting Started with Django

### Learning Goals

- Explain MVT architecture and compare it with MVC
- Summarize Django’s benefits and drawbacks 
- Install and get started with Django

### Reflection Question
#### 1. Suppose you’re a web developer in a company and need to decide if you’ll use vanilla (plain) Python for a project, or a framework like Django instead. What are the advantages and drawbacks of each?

**Vanilla Python**:
- **Advantages**:
  - Greater flexibility and control: Developers have the freedom to build everything from scratch according to specific project needs.
  - Lightweight: Since no additional libraries or frameworks are included, the development environment remains minimal and straightforward.
  - Suitable for small scripts and applications: Ideal for small projects where using a framework might be overkill.

- **Drawbacks**:
  - Increased development time: Developers need to manually handle many aspects like routing, templating, and database connections.
  - Less security: Without built-in protections, developers must be vigilant about implementing security measures.
  - Steeper learning curve for complex tasks: Tasks such as database management, user authentication, and URL routing require more effort to implement.

**Django Framework**:
- **Advantages**:
  - Rapid development: Django's "batteries-included" philosophy means it comes with many built-in features, allowing developers to build applications faster.
  - Security: Django provides built-in protections against common security threats such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).
  - Scalable and maintainable: Django encourages a clean, modular code structure, making it easier to scale and maintain large applications.

- **Drawbacks**:
  - Steeper learning curve: Django has a lot of built-in features, which can be overwhelming for beginners.
  - Potential for bloat: For small or simple projects, Django might be more than what's needed, adding unnecessary complexity.
  - Less flexibility: Django enforces a certain way of doing things (such as its ORM), which might limit developers who need more control or wish to use alternative tools.

#### 2. In your own words, what is the most significant advantage of Model View Template (MVT) architecture over Model View Controller (MVC) architecture?

The most significant advantage of the MVT architecture over MVC is that MVT abstracts much of the "Controller" logic into Django itself, allowing developers to focus more on the "Model" and "Template" aspects. In MVC, the Controller often handles the logic of how data flows between the Model and the View, which can require more manual intervention by the developer. In contrast, MVT allows Django to handle much of this automatically, simplifying the development process and making it easier to get up and running quickly.

#### 3. Now that you’ve had an introduction to the Django framework, write down three goals you have for yourself and your learning process during this Achievement. You can reflect on the following questions if it helps:

1. **Understanding Django’s Core Concepts**: I want to deepen my understanding of Django’s core components, such as models, views, and templates, and how they interact within the MVT architecture.

2. **Building Real-World Applications**: I aim to apply the knowledge gained from this achievement to build a full-fledged web application that includes features like user authentication, database integration, and deployment to a live server.

3. **Enhancing Career Prospects**: By mastering Django, I plan to position myself to work on more complex projects, possibly in a company that utilizes Django, or to offer Django-based web development services as part of my career growth.

# Exercise 2.2: Django Project Set Up

## Learning Goals

- Describe the basic structure of a Django project.
- Summarize the difference between projects and apps.
- Create a Django project and run it locally.
- Create a superuser for a Django web application.

## Reflection Questions

### 1. Suppose you’re in an interview. The interviewer gives you their company’s website as an example, asking you to convert the website and its different parts into Django terms. How would you proceed?

In Django terms, I would start by identifying the main components of the website and mapping them to Django's structure. For example:

- **Website**: The entire website can be considered the **Django project**. The project would include settings, configurations, and general URL routing.
  
- **Sections of the Website**: Each distinct section of the website, such as "Home," "Blog," "Shop," or "Contact Us," could be converted into **Django apps**. These apps are self-contained modules within the project that handle specific functionality.

- **Templates**: The HTML files used for rendering the pages would be Django **templates**, which are linked to views and are used to generate the final HTML pages.

- **Static Files**: The website's static assets like CSS, JavaScript, and images would be managed within the **static** directory of the Django project.

- **Models**: The data that drives the website, like blog posts, user profiles, or products, would be managed by Django **models**. These models would correspond to database tables.

- **Views**: The logic for handling user requests and returning the appropriate responses would be handled by Django **views**. Each view would be connected to a specific URL pattern.

### 2. In your own words, describe the steps you would take to deploy a basic Django application locally on your system.

To deploy a basic Django application locally, I would follow these steps:

1. **Set up a Virtual Environment**: First, I would create and activate a virtual environment to manage dependencies.
   
2. **Install Django**: Using pip, I would install Django within the virtual environment.
   
3. **Create a Django Project**: I would use the `django-admin startproject` command to create a new Django project.
   
4. **Run Migrations**: I would run `python manage.py migrate` to apply initial migrations and set up the database.
   
5. **Create a Superuser**: Next, I would create a superuser using the `python manage.py createsuperuser` command to manage the application from the admin interface.
   
6. **Start the Development Server**: Finally, I would start the development server with `python manage.py runserver` and access the application in the browser at `http://127.0.0.1:8000/`.

### 3. Do some research about the Django admin site and write down how you’d use it during your web application development.

The Django admin site is a powerful feature that allows developers to manage and administer their web applications easily. During web application development, I would use the Django admin site in the following ways:

- **Data Management**: I would use the admin site to easily add, update, and delete data within the database. This is especially useful during the development phase for testing purposes.
  
- **User Management**: The admin site allows me to manage user accounts, assign permissions, and create groups, which helps in controlling access to different parts of the application.
  
- **Model Administration**: I would customize the admin site to display and edit the models' fields, making it easier to manage the data entities of the application.
  
- **Monitoring and Debugging**: The admin interface provides a straightforward way to monitor changes, view logs, and perform other administrative tasks, which can be helpful in debugging issues during development.
  
- **Customization**: I can customize the admin interface to suit the needs of the project by registering models, modifying how they are displayed, and adding custom actions.


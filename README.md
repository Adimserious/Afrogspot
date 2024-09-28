## Introduction 
### Afrogspot
Welcome to Afrogspot, your go-to your premier African online grocery shop! designed to celebrate African-inspired products, art, fashion, and culture. Whether you're looking for everyday essentials or specialty items, we are here to make your shopping experience seamless and enjoyable. Our platform is designed to provide you with the best selection of authentic African products, delivered right to your doorstep. Afrogspot, where tradition meets convenience! from across the African diaspora.

Our aim is to provide a seamless shopping experience that bridges the gap between tradition and modern convenience. We are committed to offering a wide range of authentic African products—from groceries to cultural items—sourced from across the African diaspora and delivered directly to your doorstep. By doing so, Afrogspot fosters a deeper connection with African heritage while supporting communities and promoting sustainable practices.

![Am I Responsive Image]()

Link to live website: [CLICK HERE!](https://afrogspot-e3f40930991f.herokuapp.com/)

## Table of contents
  - [Introduction](#Introduction)
  - [Overview](#Overview)
  - [UX-User-Experience](#UX-User-Experience)
   - [Structural plane](#Structural-plane)
  - [Design Aesthetic](#Design-Aesthetic)
    - [Colour Scheme](#Colour-Scheme)
    - [Typography](#Typography)
    - [Visual Elements](#Visual-Elements)

- [Project planning](#Project-planning) 
  - [Agile methodology project Management with Github](#gile-methodology-project-Management-with-Github) 
     - [Repositories](#Repositories)
     - [Issues and story points allocation](#Issues-and-story-points-allocation)
     - [MoSCoW Prioritisation](#MoSCoW-Prioritisation) 
     - [Project Boards](#Project-Boards)
     - [milestones](#milestones)
     - [user stories](#user-stories)
     - [Epics](#Epics)
- [Scope plan](#Scope-plan)
- [Skeleton and surface](#Skeleton-and-surface) 
    - [wireframes](#wireframes)
- [Database Schema](#Database-Schema)
   - [Entity Relationship Diagram](#Entity-Relationship-Diagram)
   - [ERD Table overview](#ERD-Table-overview)
   - [Relationships](#Relationships)
- [Security](#Security)
   - [Data Encryption](#Data-Encryption)
   - [CSRF Tokens](#CSRF-Tokens)
   - [AllAuth](#AllAuth)
- [Features](#Features)
   - [Existing features](#Existing-features)
   - [functionality](#functionality)
   - [CRUD Functionality](#CRUD-Functionality)
- [Featue remaining to implement](#Featue-remaining-to-implement)
- [Technologies Used](#Technologies-Used)
-  [fontend](#fontend)
-  [backend](#backend)
-  [deployment](#deployment)
-  [version control](#version-control)
-  [development tools](#development-tools)
-  [libraries and frameworks](#libraries-and-frameworks)
-  [validation tools](#validation-tools)
-  [Testing](#Testing)
-  [Cloning and Forking](#Cloning-and-Forking)
-  [Credits](#Credits)

## Overview 
Here's an overview of what you can expect:

Categories: The products are grouped into different categories to make browsing easier for customers. Categories also have friendly names for better user experience.

Product list: Afrogspot features a range of products with rich descriptions, prices, discount options, stock levels, and ratings. Each product can be linked to a category and a country of origin, allowing customers to filter by region. Products also offer flexibility with custom attributes such as being vegan or gluten-free, and expiration tracking to ensure freshness.

Country: Products can be categorized by their country of origin, adding a layer of cultural and geographical relevance to the items offered.

Product Variants: Some products come with size and price variations, allowing customers to choose the best size based on their needs and budget. Each variant has its own stock and pricing information.

## UX-User-Experience
## Structural plane
1. Clear Navigation and Structure
Header with Navigation: This includes a navigation bar with links to key areas (home, new arrivals, categories, account). This remains visible as users browse, providing easy access to important pages.

Search Functionality: The search bar is central to the navigation. Making it sure prominent and functional, allowing users to find products quickly. Which includes filters for category, price, and availability.

Categories Dropdown: The category dropdown helps users explore different product types, allowing for easy exploration.

2. Seamless Product Discovery
Product List Page: The products displayed under categories or search results include thumbnails, descriptions,pricing, and links to all products in that category. 

Product Filters: There is an easy-to-use filters for product attributes like “vegan,” “gluten-free,” or by country of origin.

Product Variants: Product variants (e.g., different sizes),are displayed on the product detail page with the relevant prices and stock information.


3. Product Images: product images are of high quality and represent the authenticity of the African products sold.

4. Smooth Checkout Process
Cart and Checkout: The cart icon with the total price and item count are always visible. The checkout process is simple, with clear call-to-action buttons.

Delivery Banner: The banner promoting free delivery on orders above a 50 euros encourages users to spend more. This banner updated and visible on all pages.

5. User-Centric Account Management
Account Menu: The account dropdown menu provides options for login, profile view, and product management for superusers. These pages are simple and easy to navigate.

Profile Page: On the profile page, users are greeted with their names, view their order history, address details, and can update their information easily.

6. Back to Top Button
The back-to-top button ensures that users can quickly return to the top of the page after scrolling through long product listings.

7. Mobile-First Design
Given that a large number of users might access the site via mobile, the design is fully responsive. collapsible menus (as shown in the navigation bar) are utilized effectively for different screen sizes. Product images opens in a separate window when clicked and buttons are touch-friendly, with appropriate spacing for easy interaction on mobile devices.

8. Interactive and Engaging Footer
Social Media Integration: The footer includes social media links and a subscription option, which is great for building a community and keeping users informed. icons for Facebook, Instagram, Tiktok, WhatsApp, platforms where many African businesses thrive are present.

Newsletter Signup: A simple call-to-action for subscribing to the newsletter keeps users connected and engaged.

9. Loading Feedback and Toast Messages
The toast notifications system is in place to display feedback messages to users, such as successful actions or errors and it’s easy to understand.

## Design Aesthetic
- Color Scheme: 

![Colors image]()

Consistent Branding and Visuals
African-Inspired Design: The imagery, patterns, and color schemes reflects African culture. vibrant, warm colors of green, white, and orange, combined with traditional African patterns in the design of the home page hero image and section, users are greeted with a very attractive African shop where people are seen doing some shopping.

- Typography: There is a Clear and readable fonts, with a good contrast against the background.

- Visual Elements: relevant and high-quality images is used to enhance content.

## Project planning
[GitHub repository for issues and project planning]()


![GitHub repository for issues and project planning image]()

## Agile methodology project Management with Github 
CyberSecurity Mindset adopted the Agile methodology project Management with GitHub using GitHub's features which emphasize flexibility, collaboration, and iterative progress. Here's a comprehensive explanation of some of the features i used for the Cybersecurity Mindset blog to manage an agile project using GitHub:

### 1. Repositories

- Central Hub: Each project is stored in a GitHub repository, serving as the central hub for all project-related code, documentation, and resources.

- Version Control: GitHub provides version control, allowing teams to track changes, revert to previous versions, and collaborate efficiently on code.

### 2. Issues and story points allocation

- Task Tracking:  Issues in GitHub were used to track tasks, bugs, enhancements, and user stories. Each issue represents a piece of work that needs to be completed.
- Labels: labels are used to categorize issues by type (e.g., must have, could have, should have), priority, status (e.g., in-progress, done), and sprint.
- Assignees: Assign issues to team members to designate responsibility, in this project, it was only myself.

### 3. MoSCoW Prioritization 

1. Must have (M): These are critical requirements or tasks that are essential for the success of the project. Without these, the project would fail or be significantly compromised.

2. Should have (S): Important requirements or tasks that are not critical but have a high value. They are not absolutely necessary for the current project phase but should be included if possible.

3. Could have (C): Desirable requirements or tasks that would be beneficial if included but are not necessary. They can be deferred or dropped if time or resources are limited.

4. Won't have (W): These are the least critical requirements or tasks that will not be included in the current project phase but might be considered for future phases.

### 4. Project Boards 

- Kanban Boards: GitHub Projects provide kanban-style boards where issues can be organized into columns such as To Do, In Progress, and Done. This visualizes the workflow and progress of tasks.

### 5. Milestones

- Sprint Planning: milestones were used to represent sprints or releases. Each milestone had a due date and a collection of issues that need to be completed within the sprint even though there were room for adjustment, nothing fixed or sequencial.

- Progress Tracking: The progress of milestones were tracked by monitoring the number of completed issues versus the total number of issues.

- README: Each repository typically has a README file that provides an overview of the project, setup instructions, and other important information. This is a README file for the Afrogspot.

## User stories
User stories are a fundamental element of Agile development, focusing on the needs and experiences of end-users. They are short, simple descriptions of a feature told from the perspective of the person who desires the new capability, usually a user or customer of the system. Here is the link to the Afrogspot user stories.
[GitHub repository for Afrogspot user stories]()

## Skeleton and surface 
### Wireframes
[Figma](https://www.figma.com/) was used to design the Afrogspot.

Home page Wireframe
<details>
<summary>Click to View Home Page wireframe</summary>

![wireframes]()
</details>

Product list wireframe
<details>
<summary>Click to View Product list wireframe</summary>

![wireframes]()
</details>

Product Detail Wireframe
<details>
<summary>Click to View Product Detail wireframe</summary>

![wireframes]()
</details>

Manage Product Wireframe
<details>
<summary>Click to View Manage Product wireframe</summary>

![wireframes]()
</details>


Profile page Wireframe
<details>
<summary>Click to View Profile Page wireframe</summary>

![wireframes]()
</details>

Shoping Cart page Wireframe
<details>
<summary>Click to View Shoping Cart Page wireframe</summary>

![wireframes]()
</details>

Checkout page Wireframe
<details>
<summary>Click to View Checkout Page wireframe</summary>

![wireframes]()
</details>

## Database Schema

A database schema is the blueprint or architecture of a database, defining how data is organized and how the relationships between data are managed. Here is an overview of the key database schema used in Afrogspot

![Entity Relationship Diagram]()

An Entity-Relationship Diagram (ERD) is a visual representation of the data and its relationships within a database. It is a critical tool in database design and modeling, helping to clarify the structure and organization of data. Here is an ERD diagram representation of the Afrogspot.

## Tables Overview ERD

User: Django provides a default User model through django.contrib.auth.models.User, which can be extended if necessary. This stores information like The username, optional email  and password for the Afrogspot.

## ERD Relationships

## Security
As with most things, Security is a critical aspect, especially for a platform like Afrogspot that handles personal data.

### Data Encryption
All sensitive data, including user passwords and personal information, are encrypted using robust encryption methods to protect against unauthorized access and breaches.

### CSRF Tokens
CSRF (Cross-Site Request Forgery) tokens are included in every form to help authenticate the request with the server when the form is submitted. Absence of these tokens can leave a site vulnerable to attackers who may steal users data and use them for malicious purposes.

### AllAuth
Django AllAuth is an installable framework that takes care of the user registration and authentication process. Authentication was needed to determine when a user have signed up or signed out which controlled what content was accessible on the Afrogsot which gives store owners extra tasks such as manage products.

## Features 
## Existing Features

#### Home Page
![Home Page Screenshot]()

#### User Registration, Login, and Logout

  - New users can sign up by providing their username, email, and password. Existing users can log in using their credentials to access personalized features.

  **Registration/SignUp**
      ![Sign Up Screenshot]()

  **Login/SignIn**  
      ![Log in Screenshot]()

  **Logout/Signout**
      ![Log out Screenshot]()

#### Product Lists

  - 
  ![Product Lists Screenshot]()

#### Product Detail

  - 
  ![Product Detail Screenshot]()

#### Manage Product

  - 
  ![Manage Product Screenshot]()

#### Profile

  - 

  ![Profile Screenshot]()

#### Responsive Navigation Bar

  - 

  ![Navigation Bar Screenshot]()

#### Shopping Cart

  - 

  ![Shopping Cart Screenshot]()

#### Checkout

  - 

  ![ Checkout Screenshot]()

#### Order Comfirmation

 - 
  ![Order Comfirmation Screenshot]()

#### Footer

 - The footer is consistent across the platform and offers additional navigation options, social media links, and legal information.

  ![Footer Screenshot]()

#### Admin Panel

 - Administrators have access to a backend panel where they can manage users, Cybersecurity posts, categories, and comments.

  ![Admin Panel Screenshot]()

## Features remaining to implement

## Technologies Used
### Frontend
- [**HTML5**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5): Used for the web Structures.
- [**CSS3**](https://developer.mozilla.org/en-US/docs/Web/CSS): For Styling some of the web content.
- [**Bootstrap**](https://getbootstrap.com/): Responsive design and layout framework.


## Backend
- [**Django**](https://www.djangoproject.com/): A high-level Python web framework.
- [**Python**](https://www.python.org/): Backend programming language.
- [**SQLite**](https://www.sqlite.org/index.html) (Development) 
- [**PostgreSQL**](https://www.postgresql.org/) (Production): Database systems.


## Deployment and Version Control
- [**Git**](https://git-scm.com/): Used for version control.
- [**GitHub**](https://github.com/): Hosts the repository and facilitates version control and collaboration.
- [**Heroku**](https://www.heroku.com/): Platform as a service (PaaS) for deploying applications.
-  **Setting up on Heroku:**
    1. Create a new app on Heroku.
    2. Connect the Heroku app to the GitHub repository.
    3. Set up Config Vars in Heroku including `DATABASE_URL`, `SECRET_KEY`, `CLOUDINARY_URL`, `DISABLE_COLLECTSTATIC`, (this is temporary, and can be removed for the final deployment) etc.
    4. Deploy the main branch using the Heroku dashboard or enable automatic deployments for every push to the main branch.
**For deployment Heroku needs two additional files in order to deploy properly.**
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using:

- **pip3 install -r requirements.txt**

If you have your own packages that have been installed, then the requirements file needs updated using:

- **pip3 freeze --local > requirements.txt**

**The Procfile can be created with the following command:**

echo web: gunicorn app_name.wsgi > Procfile
replace app_name with the name of your primary Django app name; the folder where settings.py is located

## Development Tools
- [**GitPod**](https://www.gitpod.io/): Preferred IDE for writing and editing code.

## Libraries and Frameworks

- **asgiref (3.8.1)**: Supports asynchronous capabilities in Django, enabling better performance for asynchronous apps.
- **crispy-bootstrap5 (0.7)**: Allows Django forms to be styled effortlessly with Bootstrap 5, enhancing form presentation without extensive front-end coding.
- **dj-database-url (0.4.2)**: Simplifies database configuration using a URL scheme, which is especially useful for deployments on platforms like Heroku.

- **Django (4.2.11)**: The main web framework for the project, providing the necessary tools to build a secure, scalable, and maintainable web application.
- **django-allauth (0.57.2)**: Adds authentication, registration, and account management capabilities, supporting both traditional and social authentication methods.
- **django-bootstrap4 (24.1)**: Facilitates the use of Bootstrap 4 in Django templates for consistent and responsive design across the application.
- **django-crispy-forms (2.1)**: Helps in rendering Django forms in a DRY (Don't Repeat Yourself) manner, allowing form styling through template packs.
- **django-summernote (0.8.20.0)**: Provides a rich text editor for Django forms, enhancing text input fields with WYSIWYG editing capabilities.
- **gunicorn (20.1.0)**: Serves as a Python WSGI HTTP Server for UNIX, enabling Django apps to handle more concurrent traffic.
- **oauthlib (3.2.2)**: A generic implementation of OAuth for sharing authentication across services, used in conjunction with django-allauth.
- **psycopg2 (2.9.9)**: Acts as a PostgreSQL database adapter for Python, essential for database operations in Django projects using PostgreSQL.
- **PyJWT (2.8.0)**: A Python library for encoding, decoding, and verifying JSON Web Tokens (JWT), useful for stateless authentication mechanisms.
- **python3-openid (3.2.0)**: Supports Python 3 applications in implementing OpenID authentication, often used in conjunction with django-allauth.
- **requests-oauthlib (2.0.0)**: Combines the power of the `requests` library with `oauthlib` for OAuth 1 and OAuth 2 authentication of requests.
- **sqlparse (0.4.4)**: A non-validating SQL parser for Python, which provides formatting and syntax analysis for SQL scripts used within Django.
- **urllib3 (1.26.18)**: A powerful HTTP client for Python, used for making HTTP requests in various 
## Validation Tools
- [**W3C Markup Validation Service**](https://validator.w3.org/): For validating HTML5 code.
- [**W3C CSS Validation Service**](https://jigsaw.w3.org/css-validator/): For validating CSS3 code.
- [**JSHint**](https://jshint.com/): A tool that helps to detect errors and potential problems in JavaScript code.
- [**CI Python Linter**](https://pep8ci.herokuapp.com/): Analyzes Python code to look for bugs and signs of poor quality.
- [**Google Lighthouse**](https://developers.google.com/web/tools/lighthouse): For auditing performance, accessibility, and search engine optimization of web pages.

- [**Favicon.io**](https://favicon.io/): To generate favicon icons for the website.
- [**Font Awesome**](https://fontawesome.com/): Provides icons for enhancing UI/UX.

## Testing
For all testing and validation, please refer to the [TESTING.md](TESTING.md) file.

# Cloning and Forking
## Cloning the Repository
- **Local Setup:**
  1. Clone the repository: [GitHub repository](). 
 `git clone .
  2. Navigate into the project directory: `cd cybersecurity mindset`
  3. Install dependencies: `pip install -r requirements.txt`
  4. Set up local environment variables in a `.env` file.
  5. Run migrations: `python manage.py migrate`
  6. Start the development server: `python manage.py runserver`

## Forking the Repository
- **For Contributions:**
  1. Fork the repository on [GitHub repository]().
  2. Clone your forked repository to your local machine.
  3. Follow the local setup steps as above.
  4. Make changes and push them back to your fork.
  5. Create a pull request from your fork back to the original repo.

# Credits
## Code

## Media

## Acknowledgements
# Testing

This is the TESTING file for the [Afrogspot](https://afrogspot-e3f40930991f.herokuapp.com/)

Return back to the [README.md](README.md) file.

- [Testing](#testing)
  - [Testing  Table of Contents](#testing--table-of-contents)
  - [Validation](#validation)
      - [HTML Validation](#html-validation)
      - [CSS Validation](#css-validation)
      - [Python Validation](#python-validation)
      - [Lighthouse Scores](#lighthouse-scores)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation and Django Messages Implementation Testing](#user-input/form-validation-and-django-messages-implementation-testing)
    - [User Story Testing](#user-story-testing)
    - [Other Testing](#Other-Testing)
  - [Automated Testing](#automated-testing)
    - [Running the Tests](#running-the-tests)
    - [Test Database](#test-database)
    - [Importance of Testing](#importance-of-testing)
  - [Bugs](#bugs)
    - [Solved Bugs](#solved-bugs)
    - [Known Bugs](#known-bugs)
    - [Unknown Bugs](#unknown-bugs)


## Validation
To ensure that the Afrogspot meets its requirements and performs its intended functions correctly the following testing was carried out which focus on evaluating the final product to confirm that it meets the needs and expectations of the end-users.

#### HTML Validation
- **Tool Used:** [HTML W3C Markup Validator](https://validator.w3.org/)
- **Purpose:** Validates the HTML code of the application to ensure it is free from syntax errors and adheres to the standards set by the World Wide Web Consortium (W3C).
- **Process:** All HTML pages of the Afrogspot are checked through the W3C validator to identify and fix any markup errors or warnings.

**HTML Validation Results**
- **Errors** are the actual HTML issues that need to be fixed as they may affect the functionality or appearance of the website.
- **Warnings** are generally suggestions for best practices, which are not critical but could improve the code efficiency or accessibility.

![Home Page validation image](/images/home.page-html-cherker.png)

![Product Catalog](/images/catalog-html-checker.png)

![Product Detail validation image](/images/product-detail-html-checker.png)

![Cart validation image](/images/cart-html-checker.png)

![Checkout validation image](/images/checkout-html-checker.png)

![Order Confirmation validation image](/images/order-confirm-html-checker.png)

I tried to fix these warnings, these pages have the base template extended to them, i think because it requires login before accessing, the html validation didn't pick up the base template in them.
![Manage Product](/images/manage-product-html-checker.png)

![Add Product validation image](/images/add-product-html-checker.png)

![Edit Product validation image](/images/update-product-html-checker.png)

![Delete Product validation image](/images/delete-product-html-checker.png)

![Profile validation image](/images/profile-html-checker.png)

#### CSS Validation
- **Tool Used:** [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- **Purpose:** Ensures that the CSS code used across the platform adheres to the standards set by the W3C and is free of errors.
- **Process:** The CSS files are submitted to the W3C CSS Validator. Corrections are made based on feedback to improve performance and cross-browser compatibility.

![CSS Screenshot](/images/css-validatn-img.png)

#### Python Validation
- **Tool Used:** [CI Python Linter](https://pep8ci.herokuapp.com/#)
- **Purpose:** Analyzes Python source code to identify coding errors, enforce a coding standard, and look for code smells.
- **Process:** Python code within Afrogspot is analyzed with Pylint to ensure adherence to coding standards and to improve code quality.

- Afrogspot Project Module Python Validation Results**

**settings.py** 
![screenshot](/images/python-linter-settings.png)

**urls.py**
![screenshot](/images/python-linter-project-url.png)

Home Module Python Validation Results

**views.py**
![screenshot](/images/python-linter-home-views.png)

**urls.py**
![screenshot](/images/python-linter-home-urls.png)

Product Catalog Module Python Validation Results

**models.py**
![screenshot](/images/python-linter-product-model.png)

**forms.py**
![screenshot](/images/python-linter-product-forms.png)

**urls.py**
![screenshot](/images/python-linter-product-urls.png)

**admin.py**
![screenshot](/images/python-linter-product-admin.png)

Cart Module Python Validation Results

**views.py**
![screenshot](/images/python-linter-cart-views.png)

**models.py**
![screenshot](/images/python-linter-cart-model.png)

**urls.py**
![screenshot](/images/python-linter-cart-urls.png)

**admin.py**
![screenshot](/images/python-linter-cart-admin.png)

Checkout Module Python Validation Results

**forms.py**
![screenshot](/images/python-linter-checkout-forms.png)

**urls.py**
![screenshot](/images/python-linter-checkout-urls.png)

**admin.py**
![screenshot](/images/python-linter-checkout-admin.png)

Profiles Module Python Validation Results

**views.py**
![screenshot](/images/python-linter-profile-view.png)

**models.py**
![screenshot](/images/python-linter-profile-models.png)

**forms.py**
![screenshot](/images/python-linter-profile-forms.png)

**urls.py**
![screenshot](/images/python-linter-profile-urls.png)

**admin.py**
![screenshot](/images/python-linter-profile-admin.png)

#### Lighthouse Scores
- **Tool Used:** [Google Lighthouse](https://en.wikipedia.org/wiki/Google_Lighthouse)
- **Purpose:** To assess the quality of web pages in terms of performance, accessibility, progressive web apps, SEO, and best practices.
- **Process:** Afrogspot is tested with Google Lighthouse, which provides a detailed report on various aspects of the site’s performance and offers recommendations for improvement.

#### Home Page Lighthouse
![Home Page Screenshot](/images/lighthouse-home-page.png)

#### Product Lists Lighthouse
![Product Lists Screenshot](/images/lighthouse-product-catalog.png)

#### Product Detail Lighthouse
![Product Detail Screenshot](/images/lighthouse-product-detail.png)

#### Manage Product Lighthouse
![Manage Product Screenshot](/images/lighthouse-manage-product.png)

#### Profile Lighthouse
![Profile Screenshot](/images/lighthouse-profile.png)

#### Shopping Cart Lighthouse
![Shopping Cart Screenshot](/images/lighthouse-cart.png)

#### Checkout Lighthouse
![Checkout Screenshot](/images/lighthouse-checkout.png)

#### Order Comfirmation Lighthouse
![Order Comfirmation Screenshot](/images/lighthouse-order-confirm.png)


## Manual Testing
### User Input/Form Validation and Django Messages Implementation Testing

| Feature            | Tested? | Action        | Expected Outcome | Pass/Fail | Screenshots |
|--------------------|---------|---------------|------------------|-----------|-------|
| Sign up Form  | Yes     | Submit form   | User receives an email message to confirm their email, then login with their details to the Home page. | Pass      | ![screenshot](/images/email-verify-signup.png)     |
| Login Form         | Yes     | Submit credentials | User is logged in and redirected to the homepage with a pop up login confirmation with users name. | Pass      | ![screenshot](/images/signin-confirm-img.png)     |
| Profile Form          | Yes     | Updates, Creates or delete user information   | Users information is submitted and updated to their profile or deleted from profile  | Pass      | ![screenshot](/images/profile-update-confirm.png) ![screenshot](/images/profile-creatn-confirm.png)  ![screenshot](/images/profile-delete-confirm.png)   |
| Subscription Form  | Yes     | Submit form   | User receives confirmation in to different page to confirm their email and can go back to the sites homepage with a click  | Pass      | ![screenshot](/images/email-subscriptn-confirm.png)     |
| Rating Form       | Yes     | Submit Rating | Rating is added to the product with rating star count | Pass      | ![screenshot](/images/rating-confirm.img.png)     |
| Add Product Form       | Yes     | Submit new product | New product is added to existing ones. | Pass      | ![screenshot](/images/add-product-confirm.png)     |
| Sign outpage       | Yes     | Sign user out | User is signed out successfully. | Pass      | ![screenshot](/images/signout-confirm.png)     |


### User Story Testing
| User Story ID | Title | Tested? | Response | Acceptance Criteria | Pass/Fail |
|---------------|-------|---------|----------|---------------------|-----------|
| #1 | User Registration & Login | Yes | No issues | User can register with an email and password | Pass |
| #2 | Returning User Login | Yes | No issues | User is redirected to the homepage after a successful login | Pass |
| #3 | Product Catalog lists | Yes | No issues | Registered User and visitors can browse the product catalog | Pass |
| #4 | Individual Product | Yes | No issues | Users can view detailed information about a product | Pass |
| #5 | Shopping Cart Management | Yes | No issues | Users can manage their cart such as update, delete and view the details | Pass |
| #6 | Checkout Process | Yes | No issues | Users can proceed to checkout and can make purchases | Pass |
| #7 | Order confirmation | Yes | No issues | User can see an order confirmation page after purchase as well as as email confirmation | Pass |
| #8 | Payment Integration | Yes | No issues | User can pay for their order using a secure and reliable payment method | Pass |
| #9 | Order Management | Yes | No issues | Store owners can  manage orders and can fulfill customer purchases | Pass |
| #10 | User Account Management | Yes | No issues | registered user can manage their account in profile and personal information with full CRUD functionality. | Pass |
| #11 | Product Reviews | Yes | No issues | Users can  leave a review for a product they purchased | Pass |
| #12 | Search and Filtering | Yes | No issues | Users can search and filter products | Pass |
| #13 | Wish List |  |  | Not yet implemented |  |
| #14 | Notifications |  |  | Not yet implemented | Pass |
| #15 | Security and Performance | Yes | No issues | data transmitted between the user and the server is secure. | Pass |

## 404 page
- A custom 404 page to handle errors such as pages that does not exit and redirect user to the homepage.
![404 Page](/images/error-page.png)

## Automated Testing
I am not able to complete automated testing in the Afrogspot E-commerce site.

### Running the Tests

To run the automated tests for Afrogspot E-commerce site, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the root directory of the project where the `manage.py` file is located.
3. Execute the following command:
   ```bash
   python manage.py test
   ```
   This command will initiate the Django test runner, which will find and run tests written throughout the project.


### Test Database

During testing, Django creates a separate database to ensure that the tests do not interfere with the production or development database. This test database is created before the tests run and is destroyed once the tests have completed. This process ensures that the testing environment is isolated and consistent.

### Importance of Testing

Automated tests help us to:
- Quickly detect and fix bugs.
- Ensure that new features integrate seamlessly without breaking existing functionality.
- Improve code quality and maintainability.
- Build confidence in the stability of the application.

## Bugs
### Solved Bugs

### Known Bugs
I am not aware of any known bugs so far.

### Unknown Bugs
I am not aware of any unknown bugs so far.

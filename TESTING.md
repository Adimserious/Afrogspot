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
![screenshot]()

**manage.py**
![screenshot]()

**asgi.py**
![screenshot]()

**wsgi.py**
![screenshot]()

**urls.py**
![screenshot]()

Home Module Python Validation Results

**views.py**
![screenshot]()

**forms.py**
![screenshot]()

**urls.py**
![screenshot]()

**admin.py**
![screenshot]()

**apps.py**
![screenshot]()

Product Catalog Module Python Validation Results

**views.py**
![screenshot]()

**models.py**
![screenshot]()

**forms.py**
![screenshot]()

**urls.py**
![screenshot]()

**admin.py**
![screenshot]()

**apps.py**
![screenshot]()

Cart Module Python Validation Results

**views.py**
![screenshot]()

**models.py**
![screenshot]()

**urls.py**
![screenshot]()

**admin.py**
![screenshot]()

**apps.py**
![screenshot]()

Checkout Module Python Validation Results

**views.py**
![screenshot]()

**models.py**
![screenshot]()

**forms.py**
![screenshot]()

**urls.py**
![screenshot]()

**admin.py**
![screenshot]()

**apps.py**
![screenshot]()

Profiles Module Python Validation Results

**views.py**
![screenshot]()

**models.py**
![screenshot]()

**forms.py**
![screenshot]()

**urls.py**
![screenshot]()

**admin.py**
![screenshot]()

**apps.py**
![screenshot]()

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
| Sign up Form  | Yes     | Submit form   | User receives an email message to confirm their email, then login with their details to the Home page. | Pass      | ![screenshot]()     |
| Login Form         | Yes     | Submit credentials | User is logged in and redirected to the homepage with a pop up login confirmation with users name. | Pass      | ![screenshot]()     |
| Profile Form          | Yes     | Updates user information   | Users information is submitted and updated to their profile  | Pass      | ![screenshot]()     |
| Subscription Form  | Yes     | Submit form   | User receives confirmation in to different page and can go back to the sites homepage with a click  | Pass      | ![screenshot]()     |
| Rating Form       | Yes     | Submit Rating | Rating is added to the product with rating star count | Pass      | ![screenshot](/images/rating-confirm.img.png)     |
| Add Product Form       | Yes     | Submit new category | Category is added to existing ones. | Pass      | ![screenshot]()     |
| Sign outpage       | Yes     | Sign user out | User is signed out successfully. | Pass      | ![screenshot]()     |


**User Input**


### User Story Testing





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

### Unknown Bugs
I am not aware of any unknown bugs so far.

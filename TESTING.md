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

![CSS Screenshot]()

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


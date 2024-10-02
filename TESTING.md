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
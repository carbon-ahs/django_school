# [Project Name] Version Log

This document chronicles all notable changes to the [Project Name] website.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]
* **[Add new features, improvements, and fixes here before the next release]**

## [v1.2.0] - 2025-08-03
### New Features
* **User Profile Management:** Implemented a new profile management section where users can update their personal information, change their password, and upload a profile picture.
    * `apps/users/views.py`: Added `ProfileUpdateView` and `PasswordChangeView`.
    * `apps/users/urls.py`: Mapped new URLs for profile pages.
* **Search Functionality:** Added a site-wide search bar that allows users to find content across different models (e.g., blog posts, products).
    * Integrated `django-haystack` with a `Whoosh` backend.
    * Created `search/views.py` and `search/templates/`.

### Improvements
* **Performance Optimization:** Optimized database queries for the homepage and product listings, reducing page load times by ~30%.
    * `apps/products/views.py`: Replaced inefficient `for` loops with `select_related()` and `prefetch_related()` calls.
* **Template Refactoring:** Converted multiple HTML templates to use a single base template, improving consistency and maintainability.
    * `templates/base.html`: Updated with new blocks for dynamic content.
* **Image Handling:** Implemented `Pillow` for automatic resizing and compression of user-uploaded images.
    * `apps/core/models.py`: Added a `save()` method to `ImageField` models.

### Bug Fixes
* Fixed a critical bug where users were unable to reset their passwords.
    * `apps/users/views.py`: Corrected a redirect loop in the password reset process.
* Resolved an issue where the contact form was failing to send emails.
    * `apps/contact/views.py`: Ensured `EMAIL_BACKEND` settings were correctly loaded from the Django settings file.

### Security
* Applied the latest security patches for Django to mitigate against potential XSS vulnerabilities.
* Hardened CSRF protection settings by ensuring `CSRF_COOKIE_SECURE = True` in production.

---

## [v1.1.1] - 2025-07-28
### Bug Fixes
* Fixed a typo in the homepage header that displayed "Welcom" instead of "Welcome".
* Corrected an issue where the footer links were not properly navigating to their respective pages.

---

## [v1.1.0] - 2025-07-20
### New Features
* **Blog Module:** Added a complete blogging platform with support for creating, editing, and publishing articles.
    * `apps/blog/`: Created a new app with models for `Post`, `Category`, and `Tag`.
    * `templates/blog/`: Added templates for post list, detail, and category views.
* **Contact Us Page:** Implemented a functional contact form that sends user inquiries to the site administrator.
    * `apps/contact/`: Created a new app for the contact form functionality.

### Improvements
* Updated the site's styling to a more modern and clean design.
    * `static/css/styles.css`: Overhauled CSS stylesheet.
* Improved the navigation bar to be responsive on mobile devices.
    * `templates/base.html`: Added a responsive menu toggle using JavaScript.

---

## [v1.0.0] - 2025-07-01
### Initial Release
* Initial deployment of the [Project Name] website.
* Core functionality includes:
    * Homepage
    * About Us page
    * Basic user authentication (signup, login, logout)
* Deployed on a single server instance with `Gunicorn` and `Nginx`.
* Initial database schema includes `User` and `Core` models.
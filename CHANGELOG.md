# School Website Version Log

This document chronicles all notable changes to the School website.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]
* **[Add new features, improvements, and fixes here before the next release]**


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

## [v1.0.0] - 2025-08-03
### Initial Release
* Initial deployment of the School website.

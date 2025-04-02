# Day 8: Implementing Basic Forms in Django

## Overview
On Day 8, we explored Django forms and implemented a basic form handling mechanism. We focused on using Django's `forms.Form` class to create a form, process POST requests, and display user input dynamically in a template.

## Key Concepts Learned
- Creating a Django form using `forms.Form`
- Handling POST requests in a view
- Validating form data and extracting cleaned data
- Rendering forms in an HTML template

## Steps Completed
1. **Created a `forms.py` file**: Defined a `GreetingForm` with a single `username` field.
2. **Updated `views.py`**:
   - Implemented `greet_form_view`, which handles form submission.
   - Rendered the form initially and processed input upon submission.
3. **Configured templates**:
   - Created `greet_form.html` to display the form.
   - Created `greet.html` to show the personalized greeting after submission.
4. **Tested the form submission process** to ensure it successfully processed user input and displayed the correct greeting.

## Issues Faced & Fixes
- **TemplateNotFound Error**: Initially, Django could not find `greet.html`, which was resolved by ensuring it was placed correctly in the `templates/my_app/` folder.
- **Understanding Form Handling**: We initially considered separating GET and POST requests but decided to handle both in a single form structure.

## Next Steps
- Explore GET requests handling in forms.
- Improve form UI and error handling.

---

✅ *Challenge completed successfully!*


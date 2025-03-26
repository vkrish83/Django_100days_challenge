# Day 5: Static Files and Styling

## Overview
Today, we learned how to work with static files in Django, specifically focusing on CSS for styling our templates. We configured Django to serve static files properly and linked a CSS file to our HTML template to enhance the UI.

## Steps Completed

1. **Created App-Level Templates**
   - Followed the app-level templates approach for better organization.
   - Stored `greeting.html` inside `my_app/templates/my_app/`.

2. **Created and Configured Static Files**
   - Created a `static/` folder inside `my_app/`.
   - Placed `style.css` inside `my_app/static/my_app/`.

3. **Updated Django Settings**
   - Ensured `STATIC_URL = '/static/'` was correctly set.
   - Added `STATICFILES_DIRS` in `settings.py`:
     ```python
     STATICFILES_DIRS = [
         BASE_DIR / "my_app" / "static",
     ]
     ```

4. **Updated Template to Load CSS**
   - Used `{% load static %}` in `greeting.html`.
   - Linked the CSS file correctly:
     ```html
     <link rel="stylesheet" href="{% static 'my_app/style.css' %}">
     ```

5. **Verified CSS Loading**
   - Opened DevTools to check if the CSS file was loaded.
   - Resolved path issues and ensured the correct folder structure.

## Learnings
- How Django handles static files.
- Configuring `STATICFILES_DIRS` properly.
- The importance of organizing templates and static files efficiently.

---

The styling is now working! Ready for **Day 6**! 🚀

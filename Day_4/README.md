# Day 4: Django Views & URL Parameters

## 🚀 Today's Task
Today, we explored Django views and URL parameters. We enhanced our greeting functionality by making the view dynamic and allowing optional URL parameters.

---

## ✅ What We Did
1. **Created a new view** (`greet_user`) that accepts an optional `username` parameter.
2. **Updated `urls.py`** to handle both default and dynamic routes.
3. **Handled missing parameters** by setting a default value (`Guest`).
4. **Tested the view** in the browser to ensure correct responses.

---

## 📝 Steps to Implement

### 1️⃣ **Updated `views.py` to accept URL parameters**
```python
from django.http import HttpResponse

def greet_user(request, username="Guest"):
    return HttpResponse(f"Hello, {username}!")
```

### 2️⃣ **Modified `urls.py` to include a dynamic route**
```python
from django.urls import path
from .views import greet_user

urlpatterns = [
    path('greet/', greet_user, name='greet_default'),  # Default greeting
    path('greet/<str:username>/', greet_user, name='greet_user'),  # Dynamic greeting
]
```

### 3️⃣ **Tested URLs in the browser**
- ✅ `http://127.0.0.1:8000/greet/` → Displays: `Hello, Guest!`
- ✅ `http://127.0.0.1:8000/greet/John/` → Displays: `Hello, John!`

### 4️⃣ **Fixed potential issues**
- **Removed unnecessary leading slashes (`/`) in `urls.py`**.
- **Applied pending migrations** using:
  ```sh
  python manage.py migrate
  ```

---

## 📌 What to Upload to GitHub
- **Updated `views.py` and `urls.py`** with the new dynamic route.
- **`README.md`** (this file) with implementation details.

---

## 🎯 Next Steps
✅ Push changes to GitHub and mark Day 4 as complete!
💬 Let us see on Day 5 challenge! 🚀

# 🚀 Day 3: Creating a Django App & Configuring URLs

## 📌 Task Summary
- Created a new Django app named `my_app`
- Registered it in `INSTALLED_APPS`
- Defined a simple view that returns an HTTP response
- Configured URLs to route traffic to the new view
- Fixed import issues after renaming the app

---

## 🔹 Steps to Complete the Task

### 1️⃣ Create the Django App
```bash
python manage.py startapp my_app
```

### 2️⃣ Register the App in settings.py
Add the app name to INSTALLED_APPS:
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_app',
]
```

### 3️⃣ Define a View in ```my_app/views.py```
```bash
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to My_App!")
```

### 4️⃣ Create ```my_app/urls.py```
```bash
from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]
```

### 5️⃣ Update the Project URLs in ```myproject/urls.py```

```bash
from django.urls import path, include

urlpatterns = [
    path('', include('my_app.urls')),
]
```
### 6️⃣ Visit the App in Browser

Go to http://127.0.0.1:8000/
You should see:
"Welcome to My_App!" 🎉
---

### 📌 What to Upload to GitHub?

- The ```my_app/``` folder

- ```README.md``` (this file)

- Updated ```settings.py``` & ```urls.py``` files (without sensitive info)

### 🚀 Next: Proceed to Day 4! 🔥

📌 **Next Steps:**  
✅ Add this **README.md** to your **Day_3/** folder.  
✅ Push everything to **GitHub**.  
✅ Let me know when you're ready for **Day 4!** 🚀🔥
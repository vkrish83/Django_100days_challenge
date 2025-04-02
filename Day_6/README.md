# 📌 Day 6: Django Templating Language (DTL)

## 🎯 Objective
Today, we explored Django's Templating Language (DTL), which helps dynamically render HTML pages using template tags, variables, and filters. DTL is a powerful way to make templates more dynamic and interactive.

---

## 🛠️ What We Did
1. **Used Variables in Templates**
   - Passed dynamic data from views to templates using context.
   - Displayed user names and messages dynamically.

2. **Implemented Template Tags**
   - Used `{% if %}`, `{% for %}`, and `{% block %}` to control template logic.
   - Created a loop to render a list dynamically.

3. **Applied Filters in Templates**
   - Used filters like `lower`, `upper`, `default`, and `length` to manipulate text.
   - Ensured data formatting was consistent.

4. **Extended Base Templates**
   - Created a `base.html` file and extended it in other templates.
   - Used `{% block content %}` to allow content replacement in child templates.

5. **Used Static Files**
   - Linked a CSS file to improve the page styling.

---

## 📂 Folder Structure
```
Day_6/
│── myproject/
│   ├── my_app/
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── greet.html
│   │   ├── static/
│   │   │   ├── style.css
│   ├── views.py
│   ├── urls.py
│── README.md
```

---

## 📌 Key Takeaways
✅ Django templates allow separation of logic and presentation.
✅ Template tags and filters make HTML rendering dynamic.
✅ Extending templates promotes reusability and cleaner code.
✅ Static files can be linked for better styling.

---

## 📤 Next Steps
🔹 Push the changes to GitHub
🔹 Start Day 7 challenge 🚀

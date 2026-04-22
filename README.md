# 📚 Library Management System (Python)

## 🔹 Overview

This is a Command-Line Interface (CLI) based Library Management System built using Python.
It allows users to manage books, issue and return them, and calculate fines for late returns.

---

## 🔹 Features

* Add books with ID, name, author, and quantity
* View all available books
* Issue books with student name, issue date, and allowed days
* Return books with validation
* Automatic fine calculation (₹10 per day after due date)
* View issued books

---

## 🔹 Technologies Used

* Python
* datetime module

---

## 🔹 Fine Logic

* No fine if returned within allowed days
* Fine = ₹10 × late days

---

## 🔹 Testing (Important)

During development, you can simulate late returns using:

```
from datetime import timedelta
issue_date = datetime.now() - timedelta(days=10)
```

⚠️ Note:
This is only for testing. In the final system, always use:

```
issue_date = datetime.now()
```

---

## 🔹 How to Run

1. Clone the repository:
   git clone https://github.com/your-username/Library-Management-System.git

2. Go to project folder:
   cd Library-Management-System

3. Run the program:
   python library.py


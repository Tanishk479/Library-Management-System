# 📚 Library Management System (Python CLI)

---

## 🔹 Overview

A modular, Command-Line Interface (CLI) based application designed to streamline library operations.  
This system manages book inventories, tracks issued books, and automatically calculates fines using Python’s `datetime` module.

---

## 🔹 Features

- 📖 **Inventory Management**  
  Add new books with unique IDs and store them in a centralized system  

- 📊 **Real-time Availability**  
  View all available books and issued books  

- 👤 **Issuance Tracking**  
  Issue books to students with a defined time period  

- 🔁 **Return System**  
  Validate book returns and update availability  

- 💰 **Fine Calculation**  
  Automatically calculates late fees at ₹10 per day  

---

## 🔹 Project Structure

```
Library-Management-System/
│
├── main.py              # Entry point (menu-driven system)
├── add_book.py          # Add new books
├── show.py              # Display available & issued books
├── issue.py             # Issue book functionality
├── Return.py            # Return book logic
├── Calculate_fine.py    # Fine calculation logic
├── utils.py             # Stores books & issued_books data
├── README.md
└── .gitignore
```

---

## 🔹 How It Works

- Books are stored in dictionaries (`books`, `issued_books`)  
- When a book is issued:
  - It moves from available → issued  
  - Issue date and allowed days are stored  
- When returning:
  - System calculates delay using `datetime`  
  - Fine is applied if overdue  
  - Book is moved back to available  

---

## 🔹 Fine Logic

- ✅ **On-Time Return**  
  If total days ≤ allowed days → No fine  

- ❌ **Late Return**  
  Fine = (total_days - allowed_days) × ₹10  

---

## 🔹 How to Run

### 1. Clone the repository
```
git clone https://github.com/Tanishk479/Library-Management-System.git
```

### 2. Navigate to the folder
```
cd Library-Management-System
```

### 3. Run the program
```
python main.py
```

---

## 🔹 Testing & Development

To simulate late return:

```python
from datetime import datetime, timedelta

# Simulate book issued 10 days ago
issue_date = datetime.now() - timedelta(days=10)
```

⚠️ Note:  
In the actual system, `datetime.now()` is used for real-time tracking.

---

## 🛠 Technologies Used

- Python 3.x  
- datetime module  

---

## 🎯 Key Learning Outcomes

- Modular programming in Python  
- File handling and structured code design  
- Working with `datetime` and `timedelta`  
- Real-world problem solving (library system)  
- Git & GitHub workflow  

---

## 🔹 Future Improvements

- Add user authentication system 🔐  
- Store data in database (SQLite/MySQL) 💾  
- Build GUI using Tkinter 🖥️  
- Add search and filter functionality 🔍  

---

## 🔹 Author

Tanishk
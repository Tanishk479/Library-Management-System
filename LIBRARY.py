from datetime import datetime
import math

books = {}
issued_books = {}

# ADD BOOK
def add_book():
    print("\n=== ADD BOOK ===")
    book_id = input("Enter Book ID: ").strip()

    if book_id in books:
        print("⚠️ Book already exists!")
    else:

        name = input("Enter Book Name: ")
        author = input("Enter Author: ")
        quantity = int(input("Enter Quantity: "))

        books[book_id] = {
            "name": name,
            "author": author,
            "quantity": quantity
        }

        print(f"✅ '{name}' added successfully!")

# SHOW BOOKS
def show_books():
    print("\n=== AVAILABLE BOOKS ===")

    if not books:
        print("No books available.")
    else:

        for bid, data in books.items():
            print(f"[{bid}] {data['name']} by {data['author']} | Qty: {data['quantity']}")

# ISSUE BOOK
def issue_book():
    print("\n=== ISSUE BOOK ===")
    book_id = input("Enter Book ID: ")

    if book_id not in books or books[book_id]["quantity"] <= 0:
        print("❌ Book not available!")
    else:

        student = input("Enter Student Name: ")
        days = int(input("For how many days?: "))

        issue_date = datetime.now()

        books[book_id]["quantity"] -= 1

        issued_books[book_id] = {
            "student": student,
            "issue_date": issue_date,
            "days": days
        }

        print(f"✅ Book issued to {student} for {days} days.")
        print("⚠️ Fine Rule:")
        print("AFTER ISSUE DATE , FINE : ₹10 on each late day ")

# CALCULATE FINE
def calculate_fine(issue_date, allowed_days):
    from datetime import datetime

    today = datetime.now()
    total_days = (today - issue_date).days

    if total_days <= allowed_days:
        return 0

    late_days = total_days - allowed_days
    fine = late_days * 10 

    return fine

# RETURN BOOK
def return_book():
    print("\n=== RETURN BOOK ===")
    book_id = input("Enter Book ID: ")

    if book_id not in issued_books:
        print("❌ Invalid return!")
        

    else:   
        data = issued_books[book_id]

        fine = calculate_fine(data["issue_date"], data["days"])

        books[book_id]["quantity"] += 1
        issued_books.pop(book_id)

        print(f"✅ Book returned by {data['student']}")

        if fine > 0:
            print(f"💰 Late Fine: ₹{fine}")
        else:
            print("🎉 Returned on time. No fine!")

# SHOW ISSUED BOOKS
def show_issued():
    print("\n=== ISSUED BOOKS ===")

    if not issued_books:
        print("No books issued.")
    

    else:   
        for bid, data in issued_books.items():
            issue_date = data["issue_date"].strftime("%d-%m-%Y")
            print(f"[{bid}] Issued to {data['student']} on {issue_date} for {data['days']} days")

# MENU
def library():
    while True:
        print("\n========= LIBRARY SYSTEM =========")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Show Issued Books")
        print("6. Exit")

        choice = int(input("Choose option (1-6): "))


        if choice == 1:
            add_book()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            show_issued()
        elif choice == 6:
            print("👋 Thank you!")
            break
        else:
            print("❌ Invalid choice!")

library()
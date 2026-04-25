
from datetime import datetime
from utils import books, issued_books
def issue_book():
    print("\n=== ISSUE BOOK ===")
    book_id = input("Enter Book ID: ")

    if book_id not in books :
        print("❌ Book not available!")
    else:

        student = input("Enter Student Name: ")
        days = int(input("For how many days?: "))

        issue_date = datetime.now()

        issued_books[book_id] = {
            "name": books[book_id]["name"],
            "author": books[book_id]["author"],
            "student": student,
            "issue_date": issue_date,
            "days": days
        }
        books.pop(book_id)

        print(f"✅ Book name : {issued_books[book_id]['name']} issued to {student} for {days} days.")
        print("⚠️ Fine Rule:")
        print("AFTER ISSUE DATE , FINE : ₹10 on each late day ")
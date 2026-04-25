# SHOW BOOKS
from utils import books, issued_books
from datetime import datetime
def show_books():
    print("\n=== AVAILABLE BOOKS ===")

    if not books:
        print("No books available.")
    else:

        for bid, data in books.items():
            print(f"[Book_ID : {bid}] {data['name']} by {data['author']}")


def show_issued():
    print("\n=== ISSUED BOOKS ===")

    if not issued_books:
        print("No books issued.")
    

    else:   
        for bid, data in issued_books.items():
            issue_date = data["issue_date"].strftime("%d-%m-%Y")
            print(f"[Book_ID : {bid}] Issued to {data['student']} on {issue_date} for {data['days']} days")
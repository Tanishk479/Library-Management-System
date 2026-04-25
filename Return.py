# RETURN BOOK
from datetime import datetime
from utils import books, issued_books
from Calculate_fine import calculate_fine
def return_book():
    print("\n=== RETURN BOOK ===")
    book_id = input("Enter Book ID: ")

    if book_id not in issued_books:
        print("Invalid return!❌")
        
    else:   
        data = issued_books[book_id]

        fine = calculate_fine(data["issue_date"], data["days"])
        
        books[book_id] = {
            "name": data["name"],
            "author": data["author"]
        }
        issued_books.pop(book_id)
        

        print(f"✅ Book name : {books[book_id]['name']} returned by {data['student']}")

        if fine > 0:
            print(f" Late Fine: ₹{fine} 💰")
        else:
            print("🎉 Returned on time. No fine!")
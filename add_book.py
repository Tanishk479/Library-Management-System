# ADD BOOK
from utils import books
def add_book():
    print("\n=== ADD BOOK ===")
    book_id = input("Enter Book ID: ").strip()

    if book_id in books:
        print("⚠️ Book already exists!")
    else:

        name = input("Enter Book Name: ")
        author = input("Enter Author: ")
        

        books[book_id] = {
            "name": name,
            "author": author,
        }

        print(f"✅ '{name}' added successfully!")
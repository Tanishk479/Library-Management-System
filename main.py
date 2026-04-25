from add_book import add_book
from show import show_books, show_issued
from issue import issue_book
from Return import return_book

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
            print("Thank you!👋")
            break
        else:
            print("❌ Invalid choice!")

library()
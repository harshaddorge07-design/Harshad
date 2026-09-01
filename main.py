import colorama
from colorama import Fore, Back, Style, init

def menu():
    print(Fore.GREEN + '''
    1. Add book
    2.view book 
    3.search book
    4.register book
    5.issue book
    6.Exit ''')


def issue_book():
    print(Fore.GREEN + "---ISSUE BOOK---")
    customer_name = input("Enter your name sir :: ").strip()
    customer_age = input("Enter your age :: ").strip()
    customer_book = input("Enter book name :: ").strip()

    with open("customers_books.txt", "a") as file:
        customer_data = file.write(f"{customer_name}, {customer_age}, {customer_book} \n")


def search_book():
    print(Fore.GREEN + "---SEARCH BOOK---")
    search_term = input("Enter book name or author name to search :: ").strip().lower()
    
    try:
        with open("book_data.txt", "r") as file:
            book_data = file.readlines()
        
        if len(book_data) == 0:
            print(Fore.YELLOW + "No books in the library")
            return
        
        found = False
        print(Fore.GREEN + "\n--- SEARCH RESULTS ---".center(100))
        print(Fore.CYAN + f"{'Book ID':<10} {'Book Name':<20} {'Author':<20} {'Quantity':<10}")
        print(Fore.CYAN + "-" * 60)
        
        for book in book_data:
            parts = book.strip().split(",")
            book_name = parts[1].strip().lower()
            author_name = parts[2].strip().lower()
            
            if search_term in book_name or search_term in author_name:
                print(Fore.GREEN + book.strip())
                found = True
        
        print(Fore.CYAN + "-" * 60)
        
        if not found:
            print(Fore.RED + "No books found matching your search!")
    
    except FileNotFoundError:
        print(Fore.RED + "No books file found. Add some books first!")


def view_books():
    try:
        with open("book_data.txt", "r") as file:
            book_data = file.readlines()
            if len(book_data) == 0:
                print(Fore.YELLOW + "No books in the library")
            else:
                print(Fore.GREEN + "\n--- BOOKS IN LIBRARY ---".center(100))
                print(Fore.CYAN + f"{'Book ID':<10} {'Book Name':<20} {'Author':<20} {'Quantity':<10}")
                print(Fore.CYAN + "-" * 60)
                for book in book_data:
                    print(Fore.GREEN + book.strip())
                print(Fore.CYAN + "-" * 60)
    except FileNotFoundError:
        print(Fore.RED + "No books file found. Add some books first!")


def add_book():
    print(Fore.GREEN + "---ADD BOOK---")
    while True:
      book_id = input(Fore.GREEN + "Enter book ID :: ").strip()
      if book_id.isdigit():
          book_id = int(book_id)
          break
      else:
          print(Fore.RED + "Invalid Book Id \n it should br number only")
    book_name = input("Enter the book name :: ").strip()
    author_name = input("Enter author name :: ").strip()
    quantity = input("Enter Quantity :: ")
    error_message = Fore.RED + "Invalid quantity entered \n Please enter valid value "
    while True:
        if quantity.isdigit():
            if int(quantity) > 0:
                quantity = int(quantity)
                break
            else:
                print(error_message)
        else:
            print(error_message)
    print(Fore.GREEN + "---Book added successfully---".center(100))

    with open("book_data.txt", "a") as file:
        file.write(f"{book_id}, {book_name}, {author_name}, {quantity} \n ")

while True:
    menu()
    choice = input("\nEnter your choice between 1 to 6 :: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        pass
    elif choice == "5":
        issue_book() 
    elif choice == "6":
        print(Fore.CYAN + "THANK YOU for choosing our system, VISIT AGAIN")
        break
    else:
        print(Fore.RED + "Invalid Choice")



        

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


def read_books():
    with open("book_data.txt", "r") as file:
        book_data = file.readlines()
    return book_data

def add_book():
    read_books()
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
        print("View Book")
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass 
    elif choice == "6":
        print(Fore.CYAN + "THANK YOU for choosing our system, VISIT AGAIN")
        break
    else:
        print(Fore.RED + "Invalid Choice")



        

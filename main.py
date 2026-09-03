import colorama
from colorama import Fore, Back, Style, init

def menu():
    print(Fore.GREEN + '''
    1. Add book
    2.view book 
    3.search book
    4.register user
    5.issue book
    6.Exit ''')

def read_book():
    """This is a function to merely read content iof a file"""
    with open("book_data.txt", "r") as file:
        book_data = file.readlines()
    return book_data 

def add_book():
    """This is add book function. It takes book ID, book name, author, Quantity as input."""
    print(Fore.GREEN + "---ADD BOOK---")
    book_data = read_book()
    book_name = input("Enter the book name :: ").strip()
    for i in book_data:
        if book_name in i:
            print(Fore.GREEN + "The Book Already Exists")
            print(Fore.RED + "Terminting The Function")
            return False
    book_id = (len(book_data) + 1)
    author_name = input("Enter author name :: ").strip()
    print(Fore.GREEN + "Book ID is :: ", book_id)
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

def view_book():
    """Display all books stored in the file."""
    book_data = read_book()
    # if not book_data:
    #    print(Fore.YELLOW + "No BOOK found ")
    #    return
    # print(book_data)  
    for i in book_data:
       print(i.replace(",", "|"), end="")


if __name__ == "__main__": 
    while True:
        menu()
        choice = input("\nEnter your choice between 1 to 6 :: ")
        if choice == "1":
          add_book()
        elif choice == "2":
          view_book()
        elif choice == "3":
          pass#search_book()
        elif choice == "4":
          pass
        elif choice == "5":
          pass#issue_book() 
        elif choice == "6":
          print(Fore.CYAN + "THANK YOU for choosing our system, VISIT AGAIN")
          break
        else:
          print(Fore.RED + "Invalid Choice")



        

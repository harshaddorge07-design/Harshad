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

while True:
    menu()
    choice = input("\nEnter your choice between 1 to 6 :: ")
    if choice == "1":
        print("Add Book")
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

        

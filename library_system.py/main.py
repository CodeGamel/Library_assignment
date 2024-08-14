from book import Book_Operations, BookManager, book_menu
from user import UserOperations, User,user_menu
from author import AuthorOperations, author_menu
import re
from datetime import datetime
import sys

book_manager = BookManager
user_ops = UserOperations()
author_ops = AuthorOperations()

def main():
    while True:
        selection = input('''
    Welcome to the Library Management System!
    
    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit

    ''')
    

    
        if selection == '1':
                book_menu()
                bookmenu_choice = input("Please pick a section")
                if bookmenu_choice == '1':
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    genre = input("Enter book genre: ")
                    publication_date = input("Enter publication date: ")
                    book_manager.add_book(title, author, genre, publication_date)
                elif bookmenu_choice == '2':
                    book_manager.borrow_book()
                elif bookmenu_choice == '3':
                    book_manager.return_book()
                elif bookmenu_choice == '4':
                    book_manager.search_books()
                elif bookmenu_choice == '5':
                    book_manager.display_library()
                else:
                    print("Invalid choice. Please try again")
        
        elif selection == '2':
                user_menu()
                usermenu_choice = input("Please pick a section")
                if usermenu_choice == '1':
                    user_ops.make_user()
                elif usermenu_choice == '2':
                    user_ops.view_user_details()
                elif usermenu_choice == '3':
                    user_ops.display_users()
                else:
                    print("Invalid choice. Please try again")
        
        elif selection == '3':
            author_menu()
            authormenu_choice = input("Please pick a section")
            if authormenu_choice == '1':
                author_ops.add_author()
            elif authormenu_choice == '2':
                author_ops.view_author()
            elif authormenu_choice == '3':
                author_ops.display_all_authors()
            else:
                print("Invalid choice. Please try again")
            
        elif selection == '4':
            print("Thanks for using the Library Mangement System")
            sys.exit()
    
main()

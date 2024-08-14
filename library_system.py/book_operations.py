from datetime import datetime
import re
from classes_library import BookOperations
from classes_library import AuthorOperations
from classes_library import UserOperations

def calculate_age(dob):
    pattern = r'^(0[1-9]|1[0-2])/([0-2][0-9]|3[01])/\d{4}$'
        
    if not re.match(pattern, dob):
        print("Invalid date format. Please use MM/DD/YYYY.")
        return None
    
    try:
        birth_date = datetime.strptime(dob, "%m/%d/%Y")
    except ValueError:
        return None

    today = datetime.today()
    
    age = today.year - birth_date.year
    
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

def add_book(self):
        title = input("Please enter Title name: ")
        author_pattern = r'^[A-Za-z\s]+$'
        author = input("Please enter the Author's name: ")
        if author_pattern(author):
            print('Author name is valid')
        else:
            print("Invalid author name.")
            return
        
        genre_pattern = r'^[A-Za-z\s\'-]+$'
        genre = input ("Please enter the Genre: ")
        if genre_pattern(genre):
            print('Author name is valid')
        else:
            print("Invalid author name.")
            return
        publication_date = input("Please enter the publication date: ")
        book = BookOperations(title, author)
        self.library.append(book)
        self.next_id += 1
        print(f"Book '{title}' added successfully") 

def borrow_book(self):
        title = input("Please enter the book you want to borrow: ")
        try:
            for book in self.library:
                if book.title == title:
                    print ("This book is already borrowed.")
                    print("Book has been found do you want to continue? Y or N")
                    if input.strip().upper() == 'Y':
                        user = input("Enter your name: ")
                        self.borrowed_books[user] = book
                        print(f"You have borrowed '{title}")
                        return
                    elif input.strip().upper() == 'N':
                        return
        except Exception as e:
            print (f"An unexpected error occured: {e}")

def return_book(self):
    title = input ("Which book are you returning?  ")
    for title, books in self.borrowed_books:
        if books.title == title:
            del(title)
        else:
            print(f"This book was not found.")

def search_books(self):
        title = input("Which book are you looking for?  ")
        for book in self.library:
            if book.title == title:
                print(f"I have found {title} in your library! ")
            else:
                print(f"I could not find {title} in your library.")

def display_library(self):

        for books in self.library:
            print("Here is all your books: ")
            print(f'Title:  {self.title}')
            print(f'Author: {self.author}')
            print(f'Genre:  {self.genre}')
            print(f'Publication Date: {self.publication_date} ')


def book_operations(book_ops):

    while True:

      while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")
    
                
                
        if input == '1':
            add_book(book_ops) 
        elif input == '2':
            borrow_book(book_ops)
        elif input == '3':
            return_book(book_ops)
        elif input == '4':
            search_books(book_ops)
        elif input == '5':
            display_library(book_ops)
        elif input == '6':
            break
    
   
def book_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")      

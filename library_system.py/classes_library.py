import re
from datetime import datetime
from funkyfunctions import calculate_age
class Book_Operations():

    def __init__(self, book_id, title, author, genre, publication_date, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability = True
        self.borrowed = False
    
    def __str__(self):
        return f"ID: {self.book_id}, Title: '{self.title}', Author: {self.author}, Available: {self.availability}"
    
class Library(Book_Operations):

    def __init__(self):
        self.library = []
        self.next_id = 1
        self.borrowed_books = {}

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
        book = Book_Operations(title, author)
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

    def search_books(self):
        title = input("Which book are you looking for?  ")
        for book in self.library:
            if book.title == title:
                print(f"I have found {title} in your library! ")
            else:
                print(f"I could not find {title} in your library.")
    
    def return_book(self):
        title = input ("Which book are you returning?  ")
        for title, books in self.borrowed_books:
            if books.title == title:
                del(title)
            else:
                print(f"This book was not found.")
    
    def display_library(self):

        for books in self.library:
            print("Here is all your books: ")
            print(f'Title:  {self.title}')
            print(f'Author: {self.author}')
            print(f'Genre:  {self.genre}')
            print(f'Publication Date: {self.publication_date} ')

class User_Operations:

    def __init__(self, username, password, email, name, address, userID): 
        self.username = username
        self.__password = password
        self.__email = email
        self._name = name
        self.__address = address
        self.__userID = userID
        self.user = []

    def get_password(self):
        return self.__password
    def get_email(self):
        return self.__email
    def get_name(self):
        return self._name
    def get_address(self):
        return self.__address
    def get_userID(self):
        return self.__userID
    
    def make_user(self):
        self.__email = input("Enter your email: ")
        self.username = input("What will your username be? ")
        self.__password = input("What will your password be? ")
        self._name = input("Enter your name: ")
        self.__address = input("Enter your address: ")
        print(f"Congrats '{self.username}' you have created your account at the email '{self.__email}'. Welcome to the library.")
        
    def view_user_details(self):
        user = input("You must enter your password to view your details")
        if input == self.__password:  #if user enters right password they can see the account details.
            print(f"Email : {self.__email}")
            print(f"Name : {self._name}")
            print(f"Address : {self.__address}")
        else:
            print("Incorrect Password. Please try again.")
            return    
    
    def display_users(self):
        print(f"Email: {self.__email}")
        print(f"Name: {self._name}")
        print(f"Username: {self.username}")
        print(f"Address:  {self.__address}")

class Author_Operations():
    def __init__(self, authors='', DOB='', bio='', age=None):
        self.authors = authors
        self.DOB = DOB
        self.bio = bio
        self.age = age
    
    def author_info(self):
        self.authors = input("What is the authors name?")
        self.DOB = input('What is the authors date and birth?')
        self.age = calculate_age(self.DOB)
        if self.age is not None:
            print(f"The author is {self.age} years old")
        
        else:
            print("Please enter the date in the format YYYY-MM-DD.")


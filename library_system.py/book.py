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


class BookManager:

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

 

def book_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
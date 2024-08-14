class AuthorOperations():
    def __init__(self):
        self.authors = {}
        self.next_id = 1
    
    def add_author(self, name, birthdate=None, biography=None, genre=None):
        author_id = self.next_id
        self.authors[author_id] = {
            'Name': name,
            'Birthdate': birthdate,
            'Biography': biography,
            'Genre': genre
        }
        self.next_id += 1
        print(f"Author added")
    
    def author_info(self):
        name = input("What is the author's name? ")
        birthdate = input("What is the author's date of birth (YYYY-MM-DD)? ")
        age = self.calculate_age(birthdate)
        if age is not None:
            print(f"The author is {age} years old")
        else:
            print("Please enter the date in the format YYYY-MM-DD.")
        
        books = input("Please enter any books from this Author: ")
        genre = input("Please enter the Genre of this Author: ")
        bio = input("Write something about the Author: ")
        
        self.add_author(name, birthdate, bio, genre, books)
    
    def view_author(self, author_id):
        author = self.authors.get(author_id)
        if author:
            print(f"ID: {author_id}")
            print(f"Name: {author['Name']}")
            print(f"Birthdate: {author['Birthdate']}")
            print(f"Biography: {author['Biography']}")
            print(f"Genre: {author['Genre']}")
            print("-" * 20)   

    def display_all_authors(self):
        if not self.authors:
            print("No authors to display.")
        else:
            for author_id, author in self.authors.items():
                print(f"ID: {author_id}")
                print(f"Name: {author['Name']}")
                print(f"Birthdate: {author['Birthdate']}")
                print(f"Biography: {author['Biography']}")
                print(f"Genre: {author['Genre']}")
                print(f"Books: {author['Books']}")
                print("-" * 20)        

def author_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
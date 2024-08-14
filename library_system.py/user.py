class User:

    def __init__(self, username, password, email, name, address, userID): 
        self.__username = username
        self.__password = password
        self.__email = email
        self.__name = name
        self.__address = address
        self.__userID = userID
        self.user = []
        self.__borrowed_books = []

    def set_password(self, password):
        self.__password = password
    def get_email(self):
        return self.__email
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)
    def get_address(self):
        return self.__address
    def get_userID(self):
        return self.__userID

class UserOperations:
    def __init__(self):
        self.users = []

    def make_user(self):
        self.__email = input("Enter your email: ")
        self.username = input("What will your username be? ")
        self.__password = input("What will your password be? ")
        self._name = input("Enter your name: ")
        self.__address = input("Enter your address: ")
        print(f"Congrats '{self.username}' you have created your account at the email '{self.__email}'. Welcome to the library.")
        new_user = User(self.username, self.__password, self.__email, self._name, self.__address)
        self.users.append(new_user)
        self.user = []
        
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
        for users in self.user:
            print(f"Email: {self.__email}")
            print(f"Name: {self._name}")
            print(f"Username: {self.username}")
            print(f"Address:  {self.__address}")

def user_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
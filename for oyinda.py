class Book:
    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.feedback = []
        self.is_borrowed = False

    def add_feedback(self, feedback):
        self.feedback.append(feedback)

class Patron:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}
        self.authors = {}

    def add_book(self, author):
        if author not in self.authors:
            self.authors[author] = []
            print(f"Author '{author}' added to the library.")
        else:
            print(f"Author '{author}' already exists in the library.")

        while len(self.authors[author]) < 5:
            book_title = input(f"Enter book title by '{author}': ")
            if book_title:
                isbn = input(f"Enter ISBN for '{book_title}': ")
                book_instance = Book(book_title, author, "Fiction", isbn)
                self.authors[author].append(book_instance)
                self.books.append(book_instance)
                print(f"Book '{book_title}' by {author} added to the library.")
            else:
                break

    def display_books(self):
        print("Available Books:")
        print("{:<25} {:<25} {:<15}".format("Title", "Author", "ISBN"))
        print("="*65)
        for book in self.books:
            print("{:<25} {:<25} {:<15}".format(book.title, book.author, book.isbn))

    def borrow_book(self, book_title, borrower):
        found = False
        for book in self.books:
            if book.title == book_title:
                found = True
                if book.is_borrowed:
                    print(f"Sorry, '{book_title}' is already borrowed by {book.is_borrowed}.")
                else:
                    book.is_borrowed = borrower
                    print(f"Book '{book_title}' by {book.author} borrowed by {borrower}.")
        if not found:
            print(f"Book '{book_title}' is not available in the library.")

# Create a library instance
my_library = Library()

while True:
    print("\nLibrary Management Software:")
    print("1. Add Author and Books")
    print("2. Display Available Books")
    print("3. Borrow a Book")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        author = input("Enter author name: ")
        my_library.add_book(author)
    elif choice == '2':
        my_library.display_books()
    elif choice == '3':
        book_to_borrow = input("Enter the book title you want to borrow: ")
        borrower_name = input("Enter your name: ")
        my_library.borrow_book(book_to_borrow, borrower_name)
    elif choice == '4':
        print("Exiting the library management software.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

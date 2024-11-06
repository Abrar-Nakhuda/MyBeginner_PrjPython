#Personal Library Management System
import json

# Initialize the library with predefined books
library = []
 # an empty list

def add_book(title, author): # a function that has 2 parameters, title and author name,by default the book will be available
    book = {
        "title": title,
        "author": author,
        "status": "available"
    }
    library.append(book)
    print(f'Added book: "{title}" by {author}')

def check_out_book(title):
    for book in library:
        if book["title"].lower() == title.lower():
            if book["status"] == "available":
                book["status"] = "checked out"
                print(f'You have checked out: "{title}"')
                return
            else:
                print(f'Sorry, "{title}" is already checked out.')
                return
    print(f'Book titled "{title}" not found in the library.')


def return_book(title):
    for book in library:
        if book["title"].lower() == title.lower():
            if book["status"] == "checked out":
                book["status"] = "available"
                print(f'You have returned : "{title}"')
                return
            else:
                print(f'"{title}" is already available.')
    print(f'Book titled "{title}" not found in the library.')

def display_books():
    print("Debugging - Current library contents:", library)
    if not library:
        print("there are currently no books available")
        return

    print("Library Collection:")
    for book in library:
        title = book["title"]
        author = book["author"]
        status = book["status"]
        print(f'Title: "{title}", Author: {author}, Status: {status}')


def search_books(search_term):
    matches = []
    for books in library:
        if search_term.lower() in books["title"].lower() or search_term.lower() in books["author"].lower():
            matches.append(books)

    if matches:
        print(f'Books matching "{search_term}":')
        for book in matches:
            print(f'Title: "{book["title"]}", Author: {book["author"]}, Status: {book["status"]}')
    else:
        print(f'No books found with the term "{search_term}".')


def save_library():
    with open("library_data.json", "w") as file:
        json.dump(library, file)
    print("Library saved to file.")

def load_library():
    try: # Load the JSON data and populate the library list with it. Check if the file exists, and if it’s empty or missing, start with an empty library.
        with open("library_data.json", "r") as file:
            global library
            library = json.load(file)
        print("Library loaded from file.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No saved library found, starting with an empty list")
        library = []

def main_menu(): 
    load_library()

    while True:
        print("\nPersonal Library Management System")
        print("1. Add a Book")
        print("2. Check Out a Book")
        print("3. Return a Book")
        print("4. Display Books")
        print("5. Search for a Book")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
            save_library()  # Save after adding a book
        
        elif choice == "2":
            title = input("Enter book title: ")
            check_out_book(title)
            save_library()
        
        elif choice == "3":
            title = input("Enter book title: ")
            return_book(title)
            save_library()
        
        elif choice == "4":
            display_books()
        
        elif choice == "5":
            search_term = input("Enter title or author to search for: ")
            search_books(search_term)

        elif choice == "6":
            save_library()  # Save before exiting
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
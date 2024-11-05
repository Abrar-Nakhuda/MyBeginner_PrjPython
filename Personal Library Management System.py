#Personal Library Management System
import json

library = [] # an empty list

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




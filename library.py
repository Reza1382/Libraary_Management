# library.py
# Import modules
import json
import os

# Definite a empty list for overall library
books = []


def add_book(title, author, year):
    """
    This difinition add a book to the list of books.

    """
    book_info = {"title": title, "author": author, "year": year}
    books.append(book_info)
    print(
        f"The book '{title}' by '{
          author}' written in year '{year}' added to the library. 😀 \n"
    )
    save_books()


def list_books():
    """
    This definition return list of books that exist in library.

    """
    if len(books) == 0:
        print("No exist any book!")
    else:
        for index, element in enumerate(books, start=1):
            print(
                f'{index}. {element["title"]} _ {element["author"]} ({element["year"]})\n'
            )


def search_books(key):
    """
    In this definition the user enter a word and the word searched in\
    books name or authors. Then return values that have the entered word in own.
    
    """
    # key_word = input("Enter part of your book name or author: ")
    results = []
    key = key.strip()
    for element in books:
        if (key.lower() in element["title"].lower()) or (
            key.lower() in element["author"].lower()
        ):
            results.append(element)
    if len(results) == 0:
        print("Don't found any book corresponding your searched word.")
    else:
        for index, element in enumerate(results, start=1):
            print(
                f'{index}. {element["title"]} _ {element["author"]} ({element["year"]})\n'
            )


def save_books():
    """
    Saving books after closing the program.

    """
    os.makedirs("data", exist_ok=True)
    with open("data/books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4, ensure_ascii=False)


def load_books():
    """
    Loading saved books after opening the program.

    """
    if os.path.exists("data/books.json"):
        with open("data/books.json", "r", encoding="utf-8") as file:
            global books
            books = json.load(file)


load_books()


def remove_books(index):
    print("Which book do you want to remove?")
    if int(index) >= 1 and int(index) <= len(books):
        del books[int(index) - 1]
        print("The book removed successfully!")
    else:
        print("Invalid value ! Enter a valid number.")
    save_books()

# Library Management System (LMS) - Simple Python Project

A very simple **Library Management System** written in Python.  
You can add books, view all books, search by title or author, remove books, and all data is saved automatically to a file so your library stays even after you close the program.

Perfect for beginners who want to practice Python basics: lists, functions, JSON files, and simple menu programs.

## Features
- Add a new book (title, author, year)
- List all books in the library
- Search books by part of the title or author name
- Remove a book by its number
- Automatically save and load books from a JSON file (`data/books.json`)
- Easy text-based menu

## Files
- `main.py` – The main program with the menu (run this file)
- `library.py` – Contains all the functions for managing books
- `data/books.json` – Created automatically; stores your books (do not edit manually)

## How to Run
1. Make sure you have Python 3 installed.
2. Download or clone this repository.
3. Open a terminal/command prompt in the project folder.
4. Run the program:
   ```bash
   python main.py
   ```
5. Follow the menu and type the number of your choice.

## Example Menu
```
========================================
My Library! 📚
Please write your choice just in number form:
    1. Add a book
    2. See existence books
    3. Search in library 
    4. Remove book
    5. Exit from system 
```

## Requirements
- Only standard Python libraries (json, os) – no extra packages needed.

## Folder Structure After First Run
```
Library-Management-System/
├── main.py
├── library.py
└── data/
    └── books.json   (created automatically)
```

Enjoy your little library! Feel free to modify the code and add new features (like editing a book, sorting, etc.). Happy coding! 📚✨

---

**Created with ❤️ by a Python developer!**  
(December 2025)

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 22:26:45 2025

@author: LENOVO
"""
# main.py

# Add a difinition from "library.py"
from library import add_book, list_books, search_books, remove_books

print("Hello! Welcome to Library Management System (LMS).")

#add_book("Introduction to Real Analysis", "Bartle & Sherbert", "1998")
#add_book("Mathematical Analysis", "Walter Rudin", "1995")
#add_book("Philosophy", "Bertrand Russel", "1920")
while True:
    print("\n" + "="*40)  # Seperator
    print("My Library! 📚")
    choice = input("Please write your choice just in number form:\n\
        1. Add a book\n\
        2. See existence books\n\
        3. Search in library \n\
        4. Remove book\n\
        5. Exit from system \n")
    if choice == "1":
        title = input("Enter the title of book: ")
        author = input("Enter author of book: ")
        year = input("Enter the year of publishing: ")
        add_book(title, author, year)
    elif choice == "2":
        list_books()
    elif choice == "5":
        print("You exit from system; have a nice day!🎄")
        break
    elif choice == "3":
        key = input("Enter search term (title or author): ")
        search_books(key)
    elif choice == "4":
        index = input("Enter number of book for romove: ")
        remove_books(index)
    else:
        print("Error: The choosen number is invalid !")
        
        
        
        
        
        
        
        
        
        
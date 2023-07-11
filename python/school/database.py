import sqlite3 #Python code library for SQL
import os #used to check file/database path exists
import sys #required for interpreter access to system functions
import time #dramatic effect!

def db_create(): #function to create a database
    db_name = input("Enter the name for the new library database: ")
    db_name=db_name +".db" #creates database filename [adds .db]
    new_db = sqlite3.connect(db_name) #establishes connectionto database[common in SQL]
    c=new_db.cursor()#method to write or modify data in database
#the following code creates a table using SQL
#first line, creates table with identifier books, fields and data type follow in brackets
    c.execute('''CREATE TABLE Books
    (book_isbn text,
    book_title text,
    book_type text,
    book_author text)
    ''')

    new_db.commit() #save changes using the commit() function
    new_db.close() #close the connection to the database

    print("Database", db_name, " created")

    menu()

def db_modify(): #function to modify database
    db_name = input('Enter the name for the existing database:') 
    db_name = db_name + '.db'
    if os.path.isfile(db_name): #check database exists 
        modify_db = sqlite3.connect(db_name)
        c = modify_db.cursor()
        isbn = input('Enter the ISBN number:')
        title = input('Enter the book title:')
        genre = input('Enter the genre of the book')
        author = input('Enter the authors name:')
        c.execute('INSERT INTO books (book_isbn, book_title, book_type, book_author) VALUES (?, ?, ?, ?)', (isbn, title, genre, author))
        
        modify_db.commit()
        modify_db.close()
        time.sleep(1)
        print ('\nData added to database')

    else:
        print('\nDatabase does not exist\n')
        menu()
    
def db_display():
    db_name = input('Enter the name of the library database:')
    db_name=db_name+'.db'
    if os.path.isfile(db_name):
        view_db = sqlite3.connect(db_name)
        c = view_db.cursor()
        c.execute('SELECT * FROM Books')
        book_library = c.fetchall()

        for book in book_library:
            print(book)

        view_db.close()

        menu()

    else:
        print('\nDatabase does not exist\n')
        menu()
    
def menu(): #function to create a user menu
    print("\n*** Library database program ***\n")
    print("Enter 1 for a new database\n")
    print("Enter 2 to add data to an existing database\n")
    print("Enter 3 to view data from an existing database\n")
    print("Enter 4 to exit\n")
    menu_choice = input("Enter menu choice: ")

    if menu_choice =="1":
        db_create()
        
    elif menu_choice =="2":
        db_modify()
    elif menu_choice =="3":
        db_display()
    elif menu_choice =="4":
        print("\nThank you for using the database, program is finishing\n")
        return()
    else:
        print("\nInvalid choice\n")
        menu()
            
menu()
   
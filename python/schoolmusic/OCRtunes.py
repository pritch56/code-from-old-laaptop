import sqlite3 #Python code library for SQL
import os #used to check file/database path exists
import sys #required for interpreter access to system functions
from tabulate import tabulate

def Account(): #works 
    AccountName = input('what do you want your account database to be called?')
    AccountName = AccountName + '.db'
    account_db = sqlite3.connect(AccountName)
    c=account_db.cursor()
    c.execute(''' CREATE TABLE account
    (account_name,
    account_favourite_artist,
    account_favourotr_genre)
    ''')

    print('database', AccountName, 'created')
    if os.path.isfile(AccountName):
        print('database found')
        add_to_account = sqlite3.connect(AccountName)
        c = add_to_account.cursor()
        Name_account = input('Enter username:')
        genre_account = input('Enter favourite genre:')
        artist_account = input('Enter favourite artist')
        c.execute('INSERT INTO account (account_name, account_favourite_artist, account_favourotr_genre ) VALUES (?, ?, ?)', (Name_account, genre_account, artist_account))

        account_db.commit()
        account_db.close()
        print ('\nData was been stored')
        menu()
    else:
        print('\nDatabase was not found')
        menu()
    return AccountName



def create(): #works
    db_name = input("Enter the name for the new library database: ")
    db_name=db_name +".db" #creates database filename [adds .db]
    new_db = sqlite3.connect(db_name) #establishes connectionto database[common in SQL]
    c=new_db.cursor()
    c.execute('''CREATE TABLE songs
    (song_Name text,
    song_genre text,
    song_length text,
    song_author text)
    ''')

    new_db.commit() #save changes using the commit() function
    new_db.close() #close the connection to the database

    print("Database", db_name, " created")
    menu()


def AddSong(): #works
    db_name = input('Enter the name for the existing database:') 
    db_name = db_name + '.db'
    if os.path.isfile(db_name): #check database exists 
        modify_db = sqlite3.connect(db_name)
        c = modify_db.cursor()
        Name = input('what is the name of the song?')
        genre = input('Enter the genre of the song?')
        author = input('Who is the song by?')
        length = input('how long is the song in seconds?')
        c.execute('INSERT INTO songs (song_Name, song_genre, song_author, song_length) VALUES (?, ?, ?, ?)', (Name, genre, author, length))
        
        modify_db.commit()
        modify_db.close()
        print ('\nData added to database')
        menu()

    else:
        print('\nDatabase does not exist\n')
        menu()

def db_display(): #not work
    db_name = input('Enter the name of the song database:')
    db_name=db_name+'.db'
    if os.path.isfile(db_name):
        view_db = sqlite3.connect(db_name)
        c = view_db.cursor()
        c.execute('SELECT * FROM songs ORDERBY song_Name') #order the songs in assending order 
        song_library = c.fetchall()

        for songs in song_library:
            print(song)

        view_db.close()

        menu()

    else:
        print('\nDatabase does not exist\n')
        menu()




def playlist():
    print('1 = create playlist')
    print('2 = add song to playlist')
    print('3 = view playlist')

    c_or_v = input('what would you like to do?')
    if c_or_v == '1':
        playlistname = input('what is the name of your new play list?')
        playlistname=playlistname +".db" #creates database filename [adds .db]
        new_db = sqlite3.connect(playlistname) #establishes connectionto database[common in SQL]
        c=new_db.cursor()
        c.execute('''CREATE TABLE songs
        (song_Name text,
        song_genre text,
        song_length text,
        song_author text)
        ''')
        print('database created')
        new_db.commit() #save changes using the commit() function
        new_db.close()
    
    if c_or_v == '2':
        nameofplaylist = input('what is the name of the playlist?')
        new_song = input('is the song in the main database?')
        if new_song == 'yes':
            Name = input('what is the name of the song?')
            nameofplaylist = nameofplaylist + '.db'
            if os.path.isfile(nameofplaylist): #check database exists 
                modify_db = sqlite3.connect(nameofplaylist)
                c = modify_db.cursor()
                song_info = c.execute(f'SELECT * FROM songs WHERE song_Name = {Name}')
                c.execute('INSERT INTO songs (song_Name, song_genre, song_author, song_length) VALUES (?, ?, ?, ?)', (song_info))
    
    if c_or_v == '3':
        db_name = input('What is the name of the playlist?')
        db_name=db_name+'.db'
        if os.path.isfile(db_name):
            view_db = sqlite3.connect(db_name)
            c = view_db.cursor()
            c.execute('SELECT * FROM songs ORDERBY song_Name') #order the songs in assending order 
            song_library = c.fetchall()
            for songs in song_library:
                print(song)
                view_db.close()

    menu()








def menu ():
    print('1 = create account')
    print('2 = functions')
    input1 = input('what would you like to do?')
    if input1 == '1':
        Account()
    if input1 == '2':
        print('1 = create song database')
        print('2 = add song') 
        print('3 = display songs')
        print('4 = playlists') 
        print('5 = display songs by artist')
        input2 = input('what would you like to do?')
        if input2 == '1':
            create()
        if input2 == '2':
            AddSong()
        if input2 == '3':
            db_display()
        if input2 == '4':
            playlist()


menu() 
import sqlite3 #Python code library for SQL
import os #used to check file/database path exists
import random

def addDummyTrack(iterations, dbName, TableName):
    modify_db = sqlite3.connect(dbName)
    c = modify_db.cursor()

    PossibleWords = ['5', '3', 'stars','nights', 'days']
    PossibleGenres = []
    PossibleArtists = []

    for i in range(iterations):
        Name = random.choice(PossibleWords) + random.choice(PossibleWords)
        genre = random.choice(PossibleGenres)
        author = random.choice(PossibleArtists)
        length = str(random.randint(30,255))
        c.execute(f'INSERT INTO {TableName} (song_Name, song_genre, song_author, song_length) VALUES ({Name}, {genre}, {author}, {length})')
        print('added')
    c.close()


addDummyTrack(100, )

towhat = input('would you like to add songs to main or a playlist?')
if towhat == 'main':
    times = input ('how many times')
    times = int(times)
    name = input ('what is the name of the database?')
    name = name + '.db'
    if os.path.isfile(name): #check database exists 
        pass

import sqlite3
import os

dirname = os.path.dirname(os.path.abspath(__file__))
dbDir = os.path.join(dirname, '..', 'stackoverflow.db')

def createConnection():
    try: 
        connection = sqlite3.connect(dbDir)
        cursor = connection.cursor()
        return { 'cursor': cursor, 'connection': connection }
    except ConnectionError as error: return print(error)

def closeConnection(connection: sqlite3.Connection):
    connection.close()
    return print('Connection closed')

def createTable():
    database = createConnection()
    cursor = database['cursor']
    cursor.execute('CREATE TABLE questions (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT, excerpt TEXT)')
    return closeConnection(database['connection'])

def insertQuestions(questions):
    database = createConnection()
    cursor = database['cursor']
    for i, question in enumerate(questions):
        cursor.execute(
            "INSERT INTO questions VALUES (?, ?, ?)", 
            (None, question['title'].strip(), question['excerpt'].strip())
        )
        print(f'{i} - Question added to database')
    database['connection'].commit()
    return closeConnection(database['connection'])

def getQuestions():
    database = createConnection()
    cursor = database['cursor']
    rows = cursor.execute('SELECT * FROM questions').fetchall()
    closeConnection(database['connection'])

    result = []

    for idRow, titleRow, excerptRow in rows:
        result.append({ 
            'id': idRow, 
            'title': titleRow, 
            'excerpt': excerptRow 
        })

    return result
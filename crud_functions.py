import sqlite3

def initiate_db():

    connection = sqlite3.connect('prod.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("prod.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    users = cursor.fetchall()


    connection.commit()
    connection.close()
    return users

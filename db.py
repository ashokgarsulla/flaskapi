# import sqlite3

# conn = sqlite3.connect("books.sqlite")

# cursor = conn.cursor()

# sql_query = """ CREATE TABLE book (
#     id integer PRIMARY KEY,
#     author text NOT NULL,
#     language text NOT NULL,
#     tittle text NOT NULL
# )
# """
# cursor.execute(sql_query)

import pymysql

conn = pymysql.connect(
    host="sql6.freesqldatabase.com",
    database="sql6518589",
    user="sql6518589",
    password="rVEeCGK2hY",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()

sql_query = """ CREATE TABLE book (
    id integer PRIMARY KEY AUTO_INCREMENT ,
    author text NOT NULL ,
    language text NOT NULL,
    tittle text NOT NULL
)
"""

cursor.execute(sql_query)
conn.close()
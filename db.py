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

# import pymysql

# conn = pymysql.connect(
#     host="sql6.freesqldatabase.com",
#     database="sql6518589",
#     user="sql6518589",
#     password="rVEeCGK2hY",
#     charset="utf8mb4",
#     cursorclass=pymysql.cursors.DictCursor
# )

# cursor = conn.cursor()

# sql_query = """ CREATE TABLE book (
#     id integer PRIMARY KEY AUTO_INCREMENT ,
#     author text NOT NULL ,
#     language text NOT NULL,
#     tittle text NOT NULL
# )
# """

# cursor.execute(sql_query)
# conn.close()


#=================================MONGODB============================================
# import pymongo
# client = pymongo.MongoClient("mongodb+srv://flaskapi:PUzNsqDnEljVlB5s@cluster0.edwc4vt.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
# db = client.test

import pymongo

# Replace the uri string with your MongoDB deployment's connection string.
# conn_str = "mongodb+srv://flaskapi:PUzNsqDnEljVlB5s@<cluster-address>/test?retryWrites=true&w=majority"
# conn_str = "mongodb+srv://flaskapi:SUH2gc4JEWag4k1J@book.dqoatii.mongodb.net/Book?retryWrites=true&w=majority"
# conn_str = "mongodb+srv://flaskapi:test@cluster0.mgaj9yj.mongodb.net/?retryWrites=true&w=majority"
# conn_str = "mongodb+srv://flaskapi:test@cluster0.mgaj9yj.mongodb.net/?retryWrites=true&w=majority"
conn_str = "mongodb+srv://test:test@cluster0.zk7u13v.mongodb.net/?retryWrites=true&w=majority"

# set a 5-second connection timeout
# cluster = pymongo.MongoClient(conn_str,ServerSelectionTimeoutMS = 5000)
# db = cluster["test"]
# collection = db["student"]
# #these information will store 
# post = {
#     "_id" : 2,
#     "name" : "Ashok kumar"
# }
# collection.insert_one(post)
myclient = pymongo.MongoClient(conn_str,ServerSelectionTimeoutMS = 5000)
print(myclient)
db = myclient.test
# collection = db["student"]
#these information will store 
# post = {

#     "name" : "Abhinash kumar"
# }
# collection.insert_one(post)

# for db in myclient.list_databases():
#     print(db)

# import pprint
# pprint.pprint(collection.find_one())
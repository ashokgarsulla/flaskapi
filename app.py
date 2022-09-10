from flask import Flask, jsonify, request
import pymysql



app = Flask(__name__)

# making conection with db 
def db_connection():
    conn = None
    try:
        conn = pymysql.connect(
            host="sql6.freesqldatabase.com",
            database="sql6518589",
            user="sql6518589",
            password="rVEeCGK2hY",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.Error as e:
        print(e)
    return conn

@app.route('/books', methods = ['GET', 'POST'])
def books():
    conn  = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM book")
        books = [
            dict(id=raw["id"], author=raw["author"], language=raw["language"], tittle=raw["tittle"])
            for raw in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)

    if request.method == 'POST':
        new_author  = request.form["author"]
        new_lang  = request.form["language"]
        new_title  = request.form["tittle"]
        
        sql = """INSERT INTO book (author, language, tittle)
                        VALUES(%s,%s,%s)"""
        
        # new_obj = {
        #     "id": iD,
        #     "author":new_author,
        #     "language": new_lang,
        #     "title": new_title,
        # }
        cursor=cursor.execute(sql,(new_author,new_lang,new_title))
        conn.commit()
        return "created succesfully "

@app.route('/book/<int:id>', methods = ['GET', 'PUT','DELETE'])
def single_book(id):
    conn  = db_connection()
    cursor = conn.cursor()
    book = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM book WHERE id =%s",(id,))
        raws = cursor.fetchall()
        
        for r in raws:
            book = r
        
        if book is not None:
            return jsonify(book), 200
        else :
            return "somthing went wrong!", 404

    if request.method == 'PUT':
        sql = """UPDATE book SET
                 author = %s,
                 language = %s,
                 tittle = %s
                 WHERE id=%s"""
        
        new_author  = request.form["author"]
        new_lang  = request.form["language"]
        new_title  = request.form["tittle"]
  
        
        updated_book = {
            "id": id,
            "author":new_author,
            "language": new_lang,
            "title": new_title,
        }
        cursor=cursor.execute(sql,(new_author,new_lang,new_title,id))
        conn.commit()
        return jsonify(updated_book)

    if request.method == 'DELETE':
        sql ="""DELETE FROM book WHERE id=%s"""
        cursor.execute(sql,(id,))
        conn.commit()
        return f"Deleted id:{id} from book table"
# import sqlite3
# from flask import Flask, jsonify, request
# import json 
# import sqlite3


# app = Flask(__name__)

# # making conection with db 
# def db_connection():
#     conn = None
#     try:
#         conn = sqlite3.connect("books.sqlite")
#     except sqlite3.error as e:
#         print(e)
#     return conn

# @app.route('/books', methods = ['GET', 'POST'])
# def books():
#     conn  = db_connection()
#     cursor = conn.cursor()

#     if request.method == 'GET':
#         cursor = conn.execute("SELECT * FROM book")
#         books = [
#             dict(id=raw[0], author=raw[1], language=raw[2], tittle=raw[3])
#             for raw in cursor.fetchall()
#         ]
#         if books is not None:
#             return jsonify(books)

#     if request.method == 'POST':
#         new_author  = request.form["author"]
#         new_lang  = request.form["language"]
#         new_title  = request.form["tittle"]
        
#         sql = """INSERT INTO book (author, language, tittle)
#                         VALUES(?,?,?)"""
        
#         # new_obj = {
#         #     "id": iD,
#         #     "author":new_author,
#         #     "language": new_lang,
#         #     "title": new_title,
#         # }
#         cursor = conn.execute(sql,(new_author,new_lang,new_title))
#         conn.commit()
#         return f"Books with the id:{cursor.lastrowid} created succesfully "

# @app.route('/book/<int:id>', methods = ['GET', 'PUT','DELETE'])
# def single_book(id):
#     conn  = db_connection()
#     cursor = conn.cursor()
#     book = None
#     if request.method == 'GET':
#         cursor = conn.execute("SELECT * FROM book WHERE id =?",(id,))
#         raws = cursor.fetchall()
        
#         for r in raws:
#             book = r
        
#         if book is not None:
#             return jsonify(book), 200
#         else :
#             return "somthing went wrong!", 404

#     if request.method == 'PUT':
#         sql = """UPDATE book SET
#                  author = ?,
#                  language = ?,
#                  tittle = ?
#                  WHERE id=?"""
        
#         new_author  = request.form["author"]
#         new_lang  = request.form["language"]
#         new_title  = request.form["tittle"]
  
        
#         updated_book = {
#             "id": id,
#             "author":new_author,
#             "language": new_lang,
#             "title": new_title,
#         }
#         cursor = conn.execute(sql,(new_author,new_lang,new_title,id))
#         conn.commit()
#         return jsonify(updated_book)

#     if request.method == 'DELETE':
#         sql ="""DELETE FROM book WHERE id=?"""
#         conn.execute(sql,(id,))
#         conn.commit()
#         return f"Deleted id:{id} from book table"

  
# driver function
if __name__ == '__main__':

	app.run(debug = True)


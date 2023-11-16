import sqlite3
con = sqlite3.connect("studentDb.db")
print("Database opened successfully")
con.execute("create table StudentDB (username TEXT NOT NULL, password TEXT UNIQUE NOT NULL)")
print("Table created successfully")
con.close()
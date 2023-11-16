import sqlite3
con = sqlite3.connect("eventDB")
print("Database opened successfully")
con.execute("create table event (username TEXT NOT NULL, password TEXT UNIQUE NOT NULL)")
print("Table created successfully")
con.close()
from flask import *
import sqlite3

from flask import render_template

website=Flask("__name__")

@website.route('/')
def page1():
    return render_template("loginpage.html")
@website.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
   msg = "msg"
   if request.method == "POST":
     try:
        username = request.form["user"]
        password = request.form["password"]
        with sqlite3.connect("StudentDB.db") as con:
          cur = con.cursor()
          cur.execute("INSERT into StudentDB (user,password) values (?,?)",(username,password))
          con.commit()
          msg = "Student successfully Added"
     except:
         con.rollback()
         msg = "We can not add the Student to the list"
     finally:
         return render_template("success.html",msg = msg)
         con.close()

@website.route("/view")
def view():
 con = sqlite3.connect("StudentDB.db")
 con.row_factory = sqlite3.Row
 cur = con.cursor()
 cur.execute("select * from StudentDB")
 rows = cur.fetchall()
 return render_template("view.html",rows = rows)

@website.route("/delete")
def delete():
 return render_template("delete.html")
@website.route("/deleterecord",methods = ["POST"])
def deleterecord():
 user = request.form["user"]
 with sqlite3.connect("StudentDB.db") as con:
   try:
     cur = con.cursor()
     cur.execute("delete from user where id = ?",user)
     msg = "record successfully deleted"
   except:
      msg = "can't be deleted"
   finally:
      return render_template("delete_record.html",msg = msg)


@website.route("/registerform")
def second_page():
    return render_template("registration.html")




    return "username : " + entered_username + "password : " + entered_password


@website.route("/test")
def card():
    return render_template("test.html")

@website.route("/tool")
def tool():
    return render_template("tools.html")

@website.route("/abt")
def abt():
    return render_template("abtbtn.html")

@website.route("/home")
def home():
    return render_template("home.html")
@website.route("/contactus")
def contact():
    return render_template(("/contact us"))

if __name__ =='__main__':
    website.run(debug=True)
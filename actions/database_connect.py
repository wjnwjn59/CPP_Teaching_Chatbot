import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="CPPCONTENT"
)
mycursor = mydb.cursor()

def DataGet(type,object):
  mycursor.execute("SELECT CONTENT FROM CPP WHERE TYPE = {} AND OBJECT = '{}'".format(type,object))
  myresult = mycursor.fetchall()
  return str(myresult).replace("[(","").replace(",)]","")
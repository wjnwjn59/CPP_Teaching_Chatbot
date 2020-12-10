import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="CPPCONTENT"
)
def GetObject(object):
  mycursor = mydb.cursor()
  mycursor.execute("SELECT OBJECT FROM CPP WHERE OBJECT = '{}'".format(object))
  myresult = mycursor.fetchall()
  return myresult

def DataGet(type,object):
  mycursor = mydb.cursor()
  mycursor.execute("SELECT CONTENT FROM CPP WHERE TYPE = {} AND OBJECT = '{}'".format(type,object))
  myresult = mycursor.fetchall()
  return myresult





# print(DataGet(1,'comment'))



import mysql.connector

dataBase = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    passwd = 'Azegba1234567890@',
    
)

# prepare cursor Object

cursorObject = dataBase.cursor()

#Create database
cursorObject.execute("CREATE DATABASE  kizito")

print("All done!")
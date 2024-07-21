import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Saqib1327@",
)

#prepare a cursor object
cursorObject = dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE crmsoftware")

print("All done")
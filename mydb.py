import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Solo@2010MQ',
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE SoloCo")

print('All Done')













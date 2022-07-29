import mysql.connector

#establishing the connection
mydb = mysql.connector.connect(user='root', password='', host='localhost')

#Creating a cursor object using the cursor() method
cursor = mydb.cursor()

#Doping database MYDATABASE if already exists.
cursor.execute("DROP database IF EXISTS MyDatabase")

#Preparing query to create a database
sql = "CREATE database mydatabase";

#Creating a database
cursor.execute(sql)

#Retrieving the list of databases
print("List of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

#Closing the connection
mydb.close()

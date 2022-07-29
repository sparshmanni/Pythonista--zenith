import mysql.connector

#establishing the connection
mydb = mysql.connector.connect(
   user='root', password='', host='', database='mydatabase')

#Creating a cursor object using the cursor() method
cursor = mydb.cursor()

#Retrieving single row
sql = '''SELECT * from EMPLOYEE'''

#Executing the query
cursor.execute(sql)

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Closing the connection
mydb.close()

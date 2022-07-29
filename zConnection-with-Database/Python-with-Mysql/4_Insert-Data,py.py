import mysql.connector

#establishing the connection
mydb = mysql.connector.connect(
   user='root', password='', host='localhost', database='mydatabase')

#Creating a cursor object using the cursor() method
cursor = mydb.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Carl', 'jones', 20, 'M', 2000)"""

try:
   # Executing the SQL command
   cursor.execute(sql)

   # Commit your changes in the database
   mydb.commit()

except:
   # Rolling back in case of error
   mydb.rollback()

# Closing the connection
mydb.close()

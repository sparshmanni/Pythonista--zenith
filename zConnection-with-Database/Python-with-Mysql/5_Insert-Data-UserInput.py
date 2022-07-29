import mysql.connector

#establishing the connection
mydb = mysql.connector.connect(
   user='root', password='', host='localhost', database='mydatabase')

#Creating a cursor object using the cursor() method
cursor = mydb.cursor()

# Preparing SQL query to INSERT a record into the database.
insert_stmt = (
   "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)"
   "VALUES (%s, %s, %s, %s, %s)"
)

fname=input("Enter first name _ ")
lname=input("Enter last name _ ")
age=int(input("Enter your age _ "))
s=input("Enter sex _")
inc=int(input("Enter your income"))
data = (fname, lname, age, s, inc)

try:
   # Executing the SQL command
   cursor.execute(insert_stmt, data)
   
   # Commit your changes in the database
   mydb.commit()

except:
   # Rolling back in case of error
   mydb.rollback()

print("Data inserted")

# Closing the connection
mydb.close()

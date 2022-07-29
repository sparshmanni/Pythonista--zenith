import mysql.connector
from tabulate import tabulate

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='', host='localhost', database='mydatabase')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving single row
sql = '''SELECT * from EMPLOYEE'''

#Executing the query
cursor.execute(sql)

#Fetching 1st row from the table
result = cursor.fetchall()

    
print(tabulate(result, headers=['FIRST_NAME', 'LAST_NAME','AGE','SEX','INCOME'], tablefmt=''))



#Closing the connection
conn.close()

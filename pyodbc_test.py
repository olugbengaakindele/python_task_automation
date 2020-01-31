#this scripts bascially test connection to SQl Sever
import os
import pyodbc as py


server = "stayner-sql01\CRONOSSYSTEMS"
database = "Staging"


#for driver in py.drivers():
    #print(driver)

    
#conn defines the connection
conn = py.connect('Driver={ODBC Driver 13 for SQL Server}; Server= ' + server + ';Database=' + database + ';Trusted_Connection=yes;')

#cur creates connection obeject
cur = conn.cursor()
cur.execute('SELECT * FROM batches ')
a=0
for row in cur:
    print(row)
    a=a+1


print(a)
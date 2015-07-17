import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully");
conn.close()


##import sqlite3
##
##conn = sqlite3.connect('powerDown.db')
##print ("Opened database successfully");
##
##conn.execute('''CREATE TABLE COMPANY
##       (ID INT PRIMARY KEY     NOT NULL,
##       NAME           TEXT    NOT NULL,
##       AGE            INT     NOT NULL,
##       ADDRESS        CHAR(50),
##       SALARY         REAL);''')
##print ("Table created successfully");
##
##conn.close()

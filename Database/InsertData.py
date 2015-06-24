#!/usr/bin/python

#Source: Tutorialpoint

import MySQLdb

# Open database connection
db = MySQLdb.connect("147.8.212.107", "wc", "stwc1023", "testdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO employee(first_name, \
       last_name, age, sex, income) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
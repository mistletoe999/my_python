#!/usr/bin/python

#Source: Tutorialpoint

import MySQLdb

# Open database connection
db = MySQLdb.connect("147.8.212.107", "wc", "stwc1023", "testdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS employee")

# Create table as per requirement
sql = """CREATE TABLE employee (
         first_name  CHAR(20) NOT NULL,
         last_name  CHAR(20),
         age INT,  
         sex CHAR(1),
         income FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()
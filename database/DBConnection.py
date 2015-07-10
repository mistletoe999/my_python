#!/usr/bin/python

#Source: Tutorialpoint

import MySQLdb

# Open database connection
db = MySQLdb.connect("147.8.212.107", "wc", "stwc1023", "testdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()
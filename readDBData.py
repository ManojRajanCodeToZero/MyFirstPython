#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('CORVUS_TRADE_STORE_UAT.db')
print("Opened database successfully")

cursor = conn.execute("SELECT table_name FROM all_tables")
for row in cursor:
   print("table_name = ", row)

print("Operation done successfully")
conn.close()

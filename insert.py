import sqlite3

conn = sqlite3.connect("example.db")
print("opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES(1,'DEDAN',17,3450000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(2,'SAKA',22,150000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(3,'SALIBA',22,450000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(4,'TROSSARD',28,280000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(5,'GABRIEL',32,650000.00)")

conn.commit()
print("Records inserted successfully")
conn.close()

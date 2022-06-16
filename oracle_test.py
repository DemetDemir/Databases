import config
from connection import connect_db
import cx_Oracle

con = connect_db()
cur = con.cursor()

with open("Oracle_Database\HR_Database_Create_Tables_Script.sql", "r") as f:
    sql_create_hr = f.read().replace("\n", "")
print(type(sql_create_hr))

cur.execute(str(sql_create_hr))

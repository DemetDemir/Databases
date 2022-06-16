import cx_Oracle

dsn = cx_Oracle.makedsn("localhost", 1521, service_name="orcl")
connection = cx_Oracle.connect(user="DEMET", password="brot", dsn=dsn,
                               encoding="UTF-8")


username = 'DEMET'
password = 'brot'
dsn = dsn
port = 1512
encoding = 'UTF-8'


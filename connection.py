import config
import cx_Oracle

#cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_21_3")

def connect_db():
    connection = None
    try:
        connection = cx_Oracle.connect(
            user = config.username,
            password = config.password,
            dsn = config.dsn,
            encoding=config.encoding)
        

        # show the version of the Oracle Database
        print(connection.version)
        return connection
    except cx_Oracle.Error as error:
        print(error)

connect_db()
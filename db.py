import mysql.connector
import os

def connect_db():
    return mysql.connector.connect(
        host=os.environ["MYSQLHOST"],
        user=os.environ["MYSQLUSER"],
        password=os.environ["MYSQLPASSWORD"],
        database=os.environ["MYSQLDATABASE"],
        port=int(os.environ["MYSQLPORT"]),
        connection_timeout=10
    )

db = connect_db()
cursor = db.cursor()

def execute_sql(sql):
    global db, cursor
    try:
        cursor.execute(sql)
        if cursor.description:
            return cursor.fetchall()
        db.commit()
        return "Query executed successfully!"
    except mysql.connector.Error:
        # reconnect automatically
        db.close()
        db = connect_db()
        cursor = db.cursor()
        cursor.execute(sql)
        if cursor.description:
            return cursor.fetchall()
        db.commit()
        return "Reconnected & executed successfully!"

import mysql.connector
import os

db = mysql.connector.connect(
    host=os.getenv("MYSQLHOST"),
    user=os.getenv("MYSQLUSER"),
    password=os.getenv("MYSQLPASSWORD"),
    database=os.getenv("MYSQLDATABASE"),
    port=int(os.getenv("MYSQLPORT")),
)
cursor = db.cursor()

def execute_sql(sql):
    try:
        cursor.execute(sql)
        if cursor.description:
            return cursor.fetchall()
        db.commit()
        return "Query executed successfully!"
    except mysql.connector.Error as err:
        return f"Execution Error: {err}"

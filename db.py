import mysql.connector
import os

db = mysql.connector.connect(
    host=os.environ["MYSQLHOST"],
    user=os.environ["MYSQLUSER"],
    password=os.environ["MYSQLPASSWORD"],
    database=os.environ["MYSQLDATABASE"],
    port=int(os.environ["MYSQLPORT"])
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

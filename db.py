import mysql.connector
import os

db = mysql.connector.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
    port=int(os.environ["MYSQL_PORT"])
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

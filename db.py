import mysql.connector
import os
from dotenv import load_dotenv

# Load .env locally (on your laptop). On Railway this does nothing, which is fine.
load_dotenv()

# ---- MySQL connection ----
db = mysql.connector.connect(
    host=os.getenv("MYSQLHOST"),
    user=os.getenv("MYSQLUSER"),
    password=os.getenv("MYSQLPASSWORD"),
    database=os.getenv("MYSQLDATABASE"),
    port=int(os.getenv("MYSQLPORT", "3306")),
)

cursor = db.cursor()

def execute_sql(sql: str):
    """Run a single SQL statement and return either rows or a message."""
    # Clear any unread results (just in case)
    try:
        while cursor.nextset():
            pass
    except mysql.connector.Error:
        pass

    try:
        cursor.execute(sql)

        if cursor.description:  # SELECT / SHOW / etc.
            rows = cursor.fetchall()
            return rows

        db.commit()  # INSERT / UPDATE / DELETE / DDL
        return "Query executed successfully!"

    except mysql.connector.Error as err:
        return f"Execution Error: {err}"

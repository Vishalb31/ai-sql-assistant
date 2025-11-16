import mysql.connector
import os
import streamlit as st

db = mysql.connector.connect(
    host=st.secrets["MYSQLHOST"],
    user=st.secrets["MYSQLUSER"],
    password=st.secrets["MYSQLPASSWORD"],
    port=int(st.secrets["MYSQLPORT"]),
    database=st.secrets["MYSQLDATABASE"]
)

cursor = db.cursor()

def execute_sql(sql):
    try:
        # Always select DB first
        cursor.execute(f"USE {st.secrets['MYSQLDATABASE']};")

        cursor.execute(sql)

        if cursor.description:
            rows = cursor.fetchall()
            return rows
        db.commit()
        return "Query executed successfully!"

    except mysql.connector.Error as err:
        return f"Execution Error: {err}"

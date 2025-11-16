import mysql.connector
import streamlit as st
import os

db = mysql.connector.connect(
    host=st.secrets["MYSQLHOST"],
    user=st.secrets["MYSQLUSER"],
    password=st.secrets["MYSQLPASSWORD"],
    database=st.secrets["MYSQLDATABASE"],
    port=int(st.secrets["MYSQLPORT"])
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

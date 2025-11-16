import mysql.connector
import streamlit as st

db = mysql.connector.connect(
    host=st.secrets["MYSQLHOST"],
    user=st.secrets["MYSQLUSER"],
    password=st.secrets["MYSQLPASSWORD"],
    database=st.secrets["MYSQL_DATABASE"],
    port=int(st.secrets["MYSQLPORT"])
)

def execute_sql(sql):
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        if cursor.description:
            return cursor.fetchall()
        else:
            db.commit()
            return "Query executed successfully!"
    except mysql.connector.Error as err:
        return f"Execution Error: {err}"

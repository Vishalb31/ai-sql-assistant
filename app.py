import streamlit as st
import pandas as pd
from agent_sql import generate_sql
from db import execute_sql

st.set_page_config(page_title="AI SQL Assistant", layout="wide")

st.title("🤖 AI SQL Assistant (Groq + MySQL)")
st.write("Chat with your database, upload CSV/Excel, auto-create tables & export SQL history.")

# Session memory
if "history" not in st.session_state:
    st.session_state.history = []
if "sql_history" not in st.session_state:
    st.session_state.sql_history = []

# Sidebar navigation
tab = st.sidebar.radio("Navigation", ["💬 Chat", "📂 Upload Files", "📦 Export SQL History"])

# ==============================
# CHAT TAB
# ==============================
if tab == "💬 Chat":
    st.subheader("Ask database:")

    for role, message in st.session_state.history:
        with st.chat_message(role):
            st.write(message)

    prompt = st.chat_input("Ask database something...")

    if prompt:
        st.session_state.history.append(("user", prompt))
        with st.chat_message("user"):
            st.write(prompt)

        # Detect if user typed SQL manually
        if prompt.strip().lower().startswith(("select", "insert", "update", "delete", "create", "drop", "alter", "use", "truncate", "show")):
            sql = prompt
        else:
            sql = generate_sql(prompt)

        st.session_state.history.append(("assistant", sql))
        st.session_state.sql_history.append(sql)

        with st.chat_message("assistant"):
            st.code(sql, language="sql")
            result = execute_sql(sql)
            st.write("**Result:**")
            st.write(result)

# ==============================
# UPLOAD FILE TAB
# ==============================
elif tab == "📂 Upload Files":
    st.subheader("Upload CSV or Excel")

    uploaded_csv = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_csv:
        df = pd.read_csv(uploaded_csv)
        st.dataframe(df)
        st.success("CSV Loaded! Ask: create a table and insert this file")
    
    uploaded_excel = st.file_uploader("Upload Excel", type=["xlsx"])
    if uploaded_excel:
        df = pd.read_excel(uploaded_excel)
        st.dataframe(df)
        st.success("Excel Loaded! Ask: insert Excel into students table")

# ==============================
# EXPORT SQL HISTORY TAB
# ==============================
elif tab == "📦 Export SQL History":
    st.subheader("Download all SQL Queries")

    if st.session_state.sql_history:
        history_text = "\n".join(st.session_state.sql_history)
        st.download_button("⬇ Download SQL", history_text, file_name="sql_history.sql")
    else:
        st.warning("No SQL generated yet.")

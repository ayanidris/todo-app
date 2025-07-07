import streamlit as st
import function

todos=function.get_todos()

st.title("My todo app")
st.subheader("This is my todo")
st.write("This app will increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo...")

import streamlit as st
from streamlit import checkbox

import function

todos=function.get_todos()

def add_todo():
    todo1= st.session_state["new_todo"] + "\n"
    todos.append(todo1)
    function.write_todos(todos)

st.title("My todo app")
st.subheader("This is my todo")
st.write("This app will increase your productivity")

for index,todo in enumerate(todos):
    Checkbox=st.checkbox(todo,key=todo)
    if Checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_return()

st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todo(),key='new_todo')

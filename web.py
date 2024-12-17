import streamlit as st
import function


todos = function.get_todos()
def add_todo():
    todo= st.session_state['new_todo'].strip()+ '\n'
    todos.append(todo)
    function.write_todos(todos)
st.title("Mehran ToDo App")
st.subheader("This is my to do list.")
st.write("Increase your productivity!!!")


for index, todo in enumerate (todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



st.text_input(label="enter to do:", placeholder="enter to do.",
              on_change=add_todo,
              key='new_todo')
print("LOVE")

st.session_state
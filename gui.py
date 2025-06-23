
import function
import FreeSimpleGUI as sg

label=sg.Text("Type in a Todo")
input_box=sg.InputText(tooltip="Enter a todo", key='todo')
add_button=sg.Button("Add")

window= sg.Window("My To-do App",layout=[[label],
                                         [add_button,input_box]],
                                         font=('Helvetica',20))
while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos=function.get_todos()
            new_todo=values['todo']+'\n'
            todos.append(new_todo)
            function.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break


window.close()
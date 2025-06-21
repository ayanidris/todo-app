from urllib.response import addbase

import function
import FreeSimpleGUI as sg

label=sg.Text("Type in a Todo")
input_box=sg.InputText(tooltip="Enter a todo")
add_button=sg.Button("Add")

window= sg.Window("My To-do App",layout=[[label],
                                         [add_button,input_box]])
window.read()
window.close()
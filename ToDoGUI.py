import Functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type a To Do")
input_box = fsg.InputText(tooltip= "Enter a ToDo")
add_button = fsg.Button("Add")

window = fsg.Window('To Do App', layout=[[label],[input_box ,add_button]])
window.read()
window.close()
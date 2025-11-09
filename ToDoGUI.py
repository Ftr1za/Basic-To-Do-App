import Functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type a To Do")
input_box = fsg.InputText(tooltip= "Enter a ToDo", key="To DO")
add_button = fsg.Button("Add")

window = fsg.Window('To Do App',
                    layout=[[label],[input_box ,add_button]],
                    font=('Poppins', 16))
while True:
    event, values = window.read()
    match event:
        case 'Add':
            past_todo = Functions.readingfile()
            new_todo = values['To DO'] + "\n"
            past_todo.append(new_todo)
            Functions.writtingfile(past_todo)
        case fsg.WIN_CLOSED:
            break

window.close()
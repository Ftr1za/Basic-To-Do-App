import Functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type a To Do")
input_box = fsg.InputText(tooltip= "Enter a ToDo", key="To DO")
add_button = fsg.Button("Add")
list_box = fsg.Listbox(values=Functions.readingfile(), key= "Item",
                       enable_events = True, size=[45,20])
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")

window = fsg.Window('To Do App',
                    layout=[[label],[input_box ,add_button],[list_box, edit_button,complete_button],[exit_button]],
                    font=('Poppins', 16))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            past_todo = Functions.readingfile()
            new_todo = values['To DO'] + "\n"
            past_todo.append(new_todo)
            Functions.writtingfile(past_todo)
            window["Item"].update(values=past_todo)
            window["To DO"].update(value="")
        case 'Edit':
            unedited = values['Item'][0]
            edited_todo = values['To DO'] + "\n"
            past_todo = Functions.readingfile()
            index = past_todo.index(unedited)
            past_todo[index] = edited_todo
            Functions.writtingfile(past_todo)
            window["Item"].update(values=past_todo)
        case 'Complete':
            completed = values['Item'][0]
            past_todo = Functions.readingfile()
            index = past_todo.index(completed)
            past_todo.pop(index)
            Functions.writtingfile(past_todo)
            window["Item"].update(values=past_todo)
            window["To DO"].update(value="")
        case 'Item':
            window["To DO"].update(value=values['Item'][0])
        case fsg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()
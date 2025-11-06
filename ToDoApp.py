import Functions
import time

date = time.strftime("%A,%d-%M-%Y")
current = time.strftime("%I:%M%p")
print(f"DATE:{date}")
print(f"TIME:{current}")

while True:
    #getting user input and striping the spaces after input.
    user_action = input("Type add, show , edit , complete or exit:")
    user_action = user_action.strip()
    user_action = user_action.lower()

    if user_action.startswith("add"):
        #another solution: if "add" in user_action[o:4]:
        tasks = Functions.readingfile()
        task = user_action[4:] + "\n"
        tasks.append(task)
        Functions.writtingfile(tasks)


    elif user_action.startswith("show"):

        tasks = Functions.readingfile()
        for index, items in enumerate(tasks):
            index = index + 1
            items = items.strip('\n')
            structure = f"{index}.{items}"
            print(structure)
        # newtodos = [item.strip('\n') for item in tasks]


    elif user_action.startswith("edit"):

        try:
            number = int(user_action[5:])
            number = number - 1
            tasks = Functions.readingfile()
            tasks[number] = input("Enter edited to do:") + '\n'
            Functions.writtingfile(tasks)

        except ValueError:
            print("Input your task number after edit!")
            continue

        except IndexError:
            print("The number you entered is out of range!")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1
            tasks = Functions.readingfile()
            todo_to_remove = tasks[index].strip('\n')
            tasks.pop(index)
            Functions.writtingfile(tasks)
            print(f"Removed to do: {number}.{todo_to_remove}")

        except IndexError:
            print("The number you entered is out of range!")
            continue

        except ValueError:
            print("Input your task number after complete!")


    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input")

print("Thanks for using ToDoApp")

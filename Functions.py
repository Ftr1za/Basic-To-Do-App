def readingfile(filepath="todoapp.txt"):
    """opening a file and read:
     file = open("todoapp.txt", "r")
     tasks = file.readlines()
     file.close()"""
    with open(filepath, "r") as func_file:
        func_tasks = func_file.readlines()
    return func_tasks


def writtingfile(func_tasks2 , filepath="todoapp.txt"):
    """creating a new file/overwrite a existing file:
    file = open("todoapp.txt' , 'w')
    file.writelines(tasks)
    file.close()"""

    with open(filepath, "w") as func_file2:
        func_file2.writelines(func_tasks2)

if __name__ == "__main__":
    print("Hello")
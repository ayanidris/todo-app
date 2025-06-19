FILEPATH='todos.txt'

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as files:
        todos1 = files.readlines()
    return todos1


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as files:
        files.writelines(todos_arg)

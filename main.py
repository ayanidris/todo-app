import function
#Here we are importing function module from different python file
import time
#Here we are importing time standard module

now=time.strftime("%b %d,%y %H:%M:%S")
print(f"It is {now}")

while True:
    user_prompt=input("Type add, show,edit,complete and exit :")
    user_prompt=user_prompt.strip().lower()

    if user_prompt.startswith('add'):
        todo=user_prompt[4:]+"\n"
        todos=function.get_todos()
        todos.append(todo)
        function.write_todos(todos)

    elif user_prompt.startswith('show'):
        todos=function.get_todos()

        for index,item in enumerate(todos):
            item=item.strip('\n')#in order to remove extra line between the output
            print(f"{index+1}-{item}")

    elif user_prompt.startswith('complete'):
        todos=function.get_todos()

        index = int(user_prompt[9:])
        todos.pop(index-1)

        function.write_todos(todos)


    elif user_prompt.startswith('edit'):
        todos=function.get_todos()

        index = int(user_prompt[5:])
        index=index-1
        new_todo = input("Enter the new todo ")+"\n"
        todos[index]=new_todo

        function.write_todos(todos)

    elif "exit" in user_prompt:
        break
    else:
        print("Wrong command try again")

print("bye")

task_list = []
today = []
tomorrow = []
inbox = []



def add_to_list():
    choice = [
        'Inbox',
        'Today',
        'Tomorrow'
    ]
    for i in range(len(choice)):
        j = i + 1
        print(f"{j}. {choice[i]}")
    # print("Where do you want to add the task?\n")


def add_task():
    """new_task = input("What do you want to do?\n")
    add_to_list()
    status = input("task added\nDo you want to add another task? type y/n")
    if status.lower() == 'y':
        add_task()"""
    new_task = input("What do you want to do?\n")
    add_to_list()
    send_to = (input("In which list you want to add the task?\n"))
    if send_to == '1':
        inbox.append(new_task)
        print("task added!\n")
    elif send_to == '2':
        today.append(new_task)
        print("task added!\n")
    elif send_to == '3':
        tomorrow.append(new_task)
        print("task added!\n")
    else:
        print("invalid choice")


''' 

def delete_task():
    display_tasks()
    task_del = int(input("Which one you want to delete?"))
    for i in range(len(task_list)):
        task_del = i + 1
    if task_del in task_list:
        task_list.remove(task_del)
    else:
        print("item is not in list.\n")
'''


def delete_task():
    task_del = 0
    display_tasks()
    if len(task_list) == 0:
        print("And no task to delete.\n")
    else:
       # task_del = int(input("Which one do you want to delete? (Enter the task number)"))
        # Check if the task number is within the valid range
        while task_del < 1 or task_del > len(task_list):
            print("Please chose a valid option: ")
            task_del = int(input("Which one do you want to delete? (Enter the task number)"))


        del task_list[task_del - 1]
        print("task Deleted\n")


 #       if 1 <= task_del <= len(task_list):
 #          del task_list[task_del - 1]
 #           print("Task deleted.")
 #       else:
 #           print("Invalid task number. No task deleted.")


def display_tasks():
    global task_list
    add_to_list()

    c = input("Please, choose the list...")
    if c == '1':
        c = int(c)
        task_list = inbox
        print("tasks in inbox below:\n")
    elif c == '2':
        c = int(c)
        task_list = today
        print("tasks for today below:\n")
    elif c == '3':
        c = int(c)
        task_list = tomorrow
        print("tasks for tomorrow below:\n")
    else:
        print("invalid choice, please choose a valid option... \n")

    if len(task_list) == 0:
        print("Task list is empty, There's no task to display.\n")
    else:
        for i in range(len(task_list)):
            j = i + 1
            print(f"{j}. {task_list[i]}\n")


def menu():
    options = [
        "1. add new task",
        "2. Delete task",
        "3. Display task list",
        "4. Exit"
    ]
    for option in options:
        print(option)


print("Main Menu\n")
while True:

    menu()
    choice = input("Choose your option: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        delete_task()
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Exiting the task manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")

import sys
import os
from datetime import datetime

to_do_list = []

try:
    file_path = sys.argv[1]
    if os.path.exists(file_path):
        with open("to_do_list.txt", "r") as file:
            for line in file:
                to_do_list.append(line.strip())
    else:
        create_file = input("File not found. Do you want to create a new file? \
                            (yes/no): ").lower()
        if create_file == "yes":
            with open(file_path, "w") as file:
                print("New file created.")
        else:
            sys.exit("Exiting...")
except Exception as e:
    sys.exit("File not found")


while True:
    try:
        option = int(input("""
                        choose a task from the list:
                        1. Add task
                        2. Edit task
                        3. View tasks
                        4. Delete task
                        5. Exit
                        """))
        match option:
            case 1:
                task = input("Enter the task description: ")
                if task and task.lower() not in [c.split("|")[0].lower() for c in to_do_list]:
                    description = f"{task}|{datetime.now().strftime("%H:%M:%S")}"
                    to_do_list.append(description)

                else:
                    print("Task cannot be empty or already exists")
            case 2:
                while True:
                    if not to_do_list:
                        print("No task to edit")
                        break
                    index = int(input("Enter the number of the task that you wish to edit: "))
                    if 1 <= index <= len(to_do_list):
                        new_description = input("Enter the new description for the task: ")
                        if new_description.lower() not in [c.split("|")[0] for c in to_do_list]:
                            to_do_list[index-1] = f"{new_description}|{datetime.now().strftime("%H:%M:%S")}"
                            print("Task has been edited successfully.")
                            break
                        else:
                            print("Task already exists. Please enter a unique description.")
                    else:
                        print("Invalid task number")
                        break
            case 3:
                if to_do_list:
                    for i, task in enumerate(to_do_list):
                        task_description, timestamp = task.split("|")
                        print(f"{i + 1}- {task_description} (Added at: {timestamp})")
                else:
                    print("No task to display")
            case 4:
                while True:
                    if not to_do_list:
                        print("No task to delete")
                        break
                    index = int(input("Enter the number of the task that you wish to delete: "))
                    if 1 <= index <= len(to_do_list):
                        to_do_list.pop(index-1)
                        print("Task deleted successfully.")
                        break
                    else:
                        print("Invalid task number")
                        break
            case 5:
                try:
                    with open("to_do_list.txt", "w") as file:
                        for task in to_do_list:
                            file.write(task + "\n")
                    sys.exit("Exiting...")
                except Exception as e:
                    print(f"Error: {e}")
                    
    except ValueError:
        print("Choose an option from the list above...")


from asyncio import tasks
import json 
import os 
from datetime import datetime

def clearconsole():
    command = "clear"
    if os.name in ("nt", "dos"): command = "cls" 
    os.system(command)


def load_task():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def create_task():
    tasks = load_task()
    name = input("Enter the task name: ")
    description = input("Enter the task description: ")
    creation_date = datetime.now().strftime("%d/%m/%y")
    edit_date = datetime.now().strftime("%d/%m/%y")
    
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    else:
        new_id = 1

    new_task = {
        "id": new_id,
        "name": name,
        "description": description,
        "status": "Pending",
        "creation_date": creation_date,
        "edit_date": edit_date
    }
    tasks.append(new_task)  
    save_tasks(tasks)  
    print("Task created successfully!")

def edit_task():
    tasks = load_task()

    if not tasks:
        print("No tasks found")
        return
    
    try:
        task_id = int(input("Enter the ID of the task to edit"))
    except ValueError:
        print("Invalid ID. Please enter a numeric ID.")
        return
    
    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            task_found = True 
            
            print("\nEditing Task:")
            print(f"ID: {task['id']}")
            print(f"Current Name: {task['name']}")
            print(f"Current Description: {task['description']}")
            print(f"Current Status: {task['status']}")

            new_name = input("Enter new name (leave blank to keep current): ")
            new_description = input("Enter new description (leave blank to keep current): ")
            new_status = input("Enter new status (leave blank to keep current): ")

        if new_name:
            task["name"] = new_name
        if new_description:
            task["description"] = new_description
        if new_status:
            task["status"] = new_status

        task["edit_date"] = datetime.now().strftime("%d/%m/%Y")

        save_tasks(tasks)
        print("Task updated succesfully.")
        break

    if not task_found:
        print("Task not found.")

def delete_task():
    tasks = load_task() 

    if not tasks:
        print("No tasks found.")
        return

    try:
        task_id = int(input("Enter the ID of the task to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a numeric ID.")
        return

    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(tasks) == len(updated_tasks):
        print("Task not found.")
    else:
        save_tasks(updated_tasks)
        print(f"Task with ID {task_id} deleted successfully!")

def list_task():
    clearconsole()
    tasks = load_task()
    if not tasks:
        print("No tasks found")
        return
    
    print("-" * 114)
    print(" _____         _      _____             _           ")
    print("|_   _|___ ___| |_   |_   _|___ ___ ___| |_ ___ ___ ")
    print("  | | | .'|_ -| '_|    | | |  _| .'|  _| '_| -_|  _|")
    print("  |_| |__,|___|_,_|    |_| |_| |__,|___|_,_|___|_|  ")
    print("                                                    ")
    print("-" * 49,"Task List View","-" * 49)
    for task in tasks:
        print(f"\nID: {task['id']}", "///" , f"Status: {task['status']}")
        print(f"Name: {task['name']}", "///" , f"Description: {task['description']}")
        print(f"Creation Date: {task['creation_date']}", "///" , f"Edit Date: {task['edit_date']}")
        print("-" * 114)

    input("\nPress Enter to return to the main menu.")
    clearconsole()

def main_menu():
    while True: 
        print("-" * 114)
        print(" _____         _      _____             _           ")
        print("|_   _|___ ___| |_   |_   _|___ ___ ___| |_ ___ ___ ")
        print("  | | | .'|_ -| '_|    | | |  _| .'|  _| '_| -_|  _|")
        print("  |_| |__,|___|_,_|    |_| |_| |__,|___|_,_|___|_|  ")
        print("                                                    ")
        print("-" * 114 )
        print("1. Create a Tasks")
        print("")
        print("2. Edit a Tasks")
        print("")
        print("3. Delete a Tasks")
        print("")
        print("4. List Tasks")
        print("")
        print("0. Exit")  
        print("-" * 114)
        print("")
        print("")
        print("")
        print("")
        print("")
        print("-" * 114)

        option = input("Select an option: ")


        if option == "1":
            create_task()
        elif option =="2":
            edit_task()
        elif option =="3":
            delete_task()
        elif option =="4":
            list_task()
        elif option =="0":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main_menu()
import sys

def add_task(description):
    with open("tasks.txt", "a") as file:
        file.write(description + "\n")
    print(f'Task added: "{description}"')

# Function to list all tasks
def list_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if tasks:
            print("Pending tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task.strip()}")
        else:
            print("No pending tasks.")
    except FileNotFoundError:
        print("No tasks found. Start by adding a task!")

# Function to complete a task
def complete_task(task_number):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        # Validate the task number
        if 0 < task_number <= len(tasks):
            completed_task = tasks.pop(task_number - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task completed: {completed_task.strip()}")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks to complete.")

def delete_task(task_number):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        # Validate the task number
        if 0 < task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task deleted: {deleted_task.strip()}")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks to delete.")

# Main command handler
if __name__ == "__main__":
    if len(sys.argv) < 2:
       if len(sys.argv) < 2:
        print("Please provide a command with the following format:")
        print("  - To add a task: python task_manager.py add \"Task description\"")
        print("  - To list all tasks: python task_manager.py list")
        print("  - To complete a task: python task_manager.py complete [task_number]")
        print("  - To delete a task: python task_manager.py delete [task_number]")

    else:
        command = sys.argv[1]

        if command == "add" and len(sys.argv) > 2:
            add_task(" ".join(sys.argv[2:]))
        elif command == "list":
            list_tasks()
        elif command == "complete" and len(sys.argv) > 2:
            try:
                complete_task(int(sys.argv[2]))
            except ValueError:
                print("Please provide a valid task number.")
        elif command == "delete" and len(sys.argv) > 2:
            try:
                delete_task(int(sys.argv[2]))
            except ValueError:
                print("Please provide a valid task number.")
        else:
            print("Invalid command or missing arguments.")

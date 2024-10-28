# Keysight_intern_Task_2021092

# Task Management CLI Tool

A simple command-line interface (CLI) tool for managing tasks. This tool allows users to add, view, complete, and delete tasks, with task data stored persistently in a text file (`tasks.txt`).

## Features

- **Add a Task**: Add a new task with a description.
- **View Tasks**: Display a list of all pending tasks.
- **Complete a Task**: Mark a task as completed and remove it from the list.
- **Delete a Task**: Remove a specific task from the list.

## Requirements

- Python 3.x

## Usage

1. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. **Commands**:

    - **Add a Task**  
      Add a new task with a description.
      ```bash
      python task_manager.py add "Your task description"
      ```
      **Example**:
      ```bash
      python task_manager.py add "Buy groceries"
      ```

    - **View Tasks**  
      View all pending tasks.
      ```bash
      python task_manager.py list
      ```

    - **Complete a Task**  
      Mark a task as completed. Replace `[task_number]` with the task's number in the list.
      ```bash
      python task_manager.py complete [task_number]
      ```
      **Example**:
      ```bash
      python task_manager.py complete 1
      ```

    - **Delete a Task**  
      Delete a task by its number in the list. Replace `[task_number]` with the task number.
      ```bash
      python task_manager.py delete [task_number]
      ```
      **Example**:
      ```bash
      python task_manager.py delete 2
      ```

3. **Sample `tasks.txt` Format**

    The `tasks.txt` file stores each task on a new line. Each line represents a task's description.

    **Example**:
    ```
    Buy groceries
    Finish reading the book
    Complete assignment
    ```

## Notes

- Ensure to use a valid task number when using the `complete` and `delete` commands.
- Running `list` displays the current list of tasks with numbers to identify them.
- Tasks are saved in `tasks.txt`, so they persist between sessions.

## License

This project is open-source and free to use.

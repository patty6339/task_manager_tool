import json
import os

# Path to the JSON file that stores tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return {}
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("No tasks available.")
        return
    print("\nTasks:")
    for task_id, task_details in tasks.items():
        print(f"{task_id}: {task_details['name']}")

def add_task(task_id, task_name, tasks):
    """Add a new task with a unique ID."""
    if task_id in tasks:
        print(f"Task ID {task_id} already exists. Please use a unique ID.")
    else:
        tasks[task_id] = {"name": task_name}
        print(f"Task '{task_name}' added successfully with ID {task_id}.")

def main():
    tasks = load_tasks()
    display_tasks(tasks)

    task_id = input("\nEnter a unique task ID: ").strip()
    task_name = input("Enter the task description: ").strip()
    add_task(task_id, task_name, tasks)

    save_tasks(tasks)
    print("\nUpdated task list:")
    display_tasks(tasks)

if __name__ == "__main__":
    main()

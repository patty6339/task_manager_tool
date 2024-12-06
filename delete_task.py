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

def delete_task(task_id, tasks):
    """Delete a task by ID."""
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Task {task_id} not found.")

def main():
    tasks = load_tasks()
    display_tasks(tasks)

    task_id = input("\nEnter the ID of the task to delete: ").strip()
    delete_task(task_id, tasks)

    save_tasks(tasks)
    print("\nUpdated task list:")
    display_tasks(tasks)

if __name__ == "__main__":
    main()

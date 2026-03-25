import json
import sys
import os
from datetime import datetime

FILE_PATH = 'tasks.json'

# 1. Load tasks
def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# 2. Save tasks
def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

# 3. Main logic
def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py [add | list | update | delete | mark-in-progress | mark-done]")
        return

    command = sys.argv[1].lower()
    tasks = load_tasks()

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: add <description>")
            return

        description = " ".join(sys.argv[2:])
        new_task = {
            "id": len(tasks) + 1,
            "description": description,
            "status": "todo",
            "createdAt": datetime.now().isoformat(),
            "updateAt": datetime.now().isoformat()
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task added successfully (ID: {new_task['id']})")

    elif command == "list":
        status_filter = sys.argv[2] if len(sys.argv) > 2 else None
        for t in tasks:
            if status_filter is None or t['status'] == status_filter:
                print(f"[{t['id']}] {t['description']} - Status: {t['status']}")

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: update <id> <new description>")
            return

        task_id = int(sys.argv[2])
        new_desc = " ".join(sys.argv[3:])

        for t in tasks:
            if t['id'] == task_id:
                t['description'] = new_desc
                t['updateAt'] = datetime.now().isoformat()

        save_tasks(tasks)
        print("Task updated.")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: delete <id>")
            return

        task_id = int(sys.argv[2])
        tasks = [t for t in tasks if t['id'] != task_id]
        save_tasks(tasks)
        print("Task deleted.")

    elif command in ["mark-in-progress", "mark-done"]:
        if len(sys.argv) < 3:
            print("Usage: mark-in-progress <id> OR mark-done <id>")
            return

        task_id = int(sys.argv[2])
        new_status = "in-progress" if command == "mark-in-progress" else "done"

        for t in tasks:
            if t['id'] == task_id:
                t['status'] = new_status
                t['updateAt'] = datetime.now().isoformat()

        save_tasks(tasks)
        print(f"Task marked as {new_status}.")

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()

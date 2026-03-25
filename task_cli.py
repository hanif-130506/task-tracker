import json
import sys
import os
from datetime import datetime

FILE_PATH = 'tasks.json'

#1. Helper : load data from the JSON file
def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
                return []
                
#2. Helper : Save data to the JSON file
def save_tasks():
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)           
        
                          
#3. Main logic
def main():
    # sys.argv collects command line arguments
    # [script_name, command, first.arg, second.arg...]    
    if len(sys.argv) < 2:
        print("Usage python python task_cli.py [add | list | update | delete | mark-in-progress | mark-done]")
        return
        
    command = sys.argv[1].lower()
    tasks = load_tasks()
    
    if command == "add":
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
        print(f"Task added successfuly (ID : {new_task['id']})")
        
    elif command == "list":
     	status_filter = sys.argv[2] if len(sys.argv) > 2 else None
     	for t in tasks:
     	    if status_filter is None or t['status'] == status_filter:
     	        print(f"[{t['id']}] {t['description']} - Status : {t['status']} ")
     	        
     	        
    elif command == "update":
          task_id = int(sys.argv[2])
          new_desc = " ".join(sys.argv[3:])
          for t in tasks:
              if t['id'] == task_id:
                  t['description'] = new_desc
                  t['updateAt'] = datetime.now().isoformat
          save_tasks(tasks)
          print("Task updated.")
          
    elif command == "delete":
              task_id = int(sys.argv[2])
              tasks = [t for t in tasks if t['id'] != task_id]
              save_tasks(tasks)
              print("Task deleted.")
              
    elif command in ["mark-in-progress", "mark-done"]:
              new_status = "in-progress" in progress if command == "mark-in-progress" else "done"
              task_id = int(sys.argv[2])
              for t in tasks:
                  if t['id'] == task_id:
                      t['status'] = new_status
                      t['updateAt'] = datetime.now().isoformat()
              save_tasks(tasks)
              print(f"Task marked as {new_status}.")
              
              
if __name__ == "__main__":
              main()    
              
        
                                                                                                                    
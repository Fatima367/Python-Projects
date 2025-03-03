import click # a library to create cli
import json # to save and load tasks from a file
import os # to check if the file exists

TODO_FILE = "todo.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
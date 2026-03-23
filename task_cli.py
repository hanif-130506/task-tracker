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
        except:
            return json.JSONDecodeError:
                return []
                
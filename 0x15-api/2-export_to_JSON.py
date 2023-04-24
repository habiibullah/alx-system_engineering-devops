#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
Export this data to JSON
"""
from sys import argv
import json
import requests


def to_json():
    """return API data"""
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in users.json():
        if user.get('id') == int(argv[1]):
            USERNAME = (user.get('username'))
            break
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((todo.get('completed'), todo.get('title')))

    """export to json"""
    todo = []
    for task in TASK_STATUS_TITLE:
        todo.append({"task": task[1], "completed": task[0], "username": USERNAME})
    data = {str(argv[1]): todo}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    to_json()


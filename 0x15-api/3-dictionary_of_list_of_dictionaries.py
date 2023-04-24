#!/usr/bin/python3
"""
Request from API; Return TODO list progress of all employees
Export this data to JSON
"""
import json
import requests


def all_to_json():
    """return API data"""
    USERS = []
    userss = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in userss.json():
        USERS.append((user.get('id'), user.get('username')))
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        TASK_STATUS_TITLE.append((todo.get('userId'),
                                  todo.get('completed'),
                                  todo.get('title')))

    """export to json"""
    data = dict()
    for u in USERS:
        todo = []
        for task in TASK_STATUS_TITLE:
            if task[0] == u[0]:
                todo.append({"task": task[2], "completed": task[1],
                          "username": u[1]})
        data[str(u[0])] = todo
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)


if __name__ == "__main__":
    all_to_json()


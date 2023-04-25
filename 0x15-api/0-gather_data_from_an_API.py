#!/usr/bin/python3
"""fetching json data from an api"""

import requests
from sys import argv

if __name__ == "__main__":
    users_id = argv[1]
    users_url = "https://jsonplaceholder.typicode.com/users/" + users_id
    users_dict = requests.get(users_url).json()
    users_name = users_dict.get("name")
    users_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    users_todo = users_todo.json()
    todo_total = 0
    completed_titles = []
    number_completed = 0

    for item in users_todo:
        if item.get("userId") == int(users_id):
            todo_total += 1
            if item.get("completed") is True:
                number_completed += 1
                completed_titles.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        users_name, number_completed, todo_total))
    for title in completed_titles:
        print("\t {}".format(title))

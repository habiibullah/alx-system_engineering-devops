#!/usr/bin/python3
"""fetching json data from an api"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    users_id = argv[1]
    users_url = "https://jsonplaceholder.typicode.com/users/" + users_id
    users_dict = requests.get(users_url).json()
    users_name = users_dict.get("username")
    users_todo = requests.get("{}/todos".format(users_url))
    users_todo = users_todo.json()
    file_names = users_id + ".csv"

    with open(file_names, 'w') as csvfile:
        for item in users_todo:
            csvfile.write('"{}","{}","{}","{}"\n'.format(item.get(
                "userId"), users_name, item.get("completed"),
                item.get("title")))


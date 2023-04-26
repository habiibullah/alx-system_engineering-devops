#!/usr/bin/python3
"""Export data from an API to CSV format.
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    # Checks if the argument can be converted to a number
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    # Main formatted names to API urls and filenames
    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_url = '{user_url}/todos'.format(user_url=user_url)
    filename = '{emp_id}.csv'.format(emp_id=emp_id)

    # User Response
    res = requests.get(user_url).json()

    # Username of the employee
    username = res.get('username')

    # User TODO Response
    res = requests.get(todo_url).json()

    # Create the new file for the user to save the information
    # Filename example: `{user_id}.csv`
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for elem in res:
            # Completed or non-completed task
            status = elem.get('completed')

            # The task name
            title = elem.get('title')

            # Writing each result of API response in a row of a CSV file
            writer.writerow([emp_id, username, status, title])


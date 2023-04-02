#!/usr/bin/python3

import json
import requests
import sys

if __name__ == '__main__':
    """Document"""

    user = requests.\
        get('https://jsonplaceholder.typicode.com/users/{}'.
            format(sys.argv[1]))
    user = user.json()
    todos = requests.\
        get('https://jsonplaceholder.typicode.com/todos?userId={}'.
            format(sys.argv[1]))
    todos = todos.json()
    name = user['name']
    total_tasks = len(todos)
    tasks_done = 0
    lists_of_titles = []
    for f in todos:
        if user['id'] == f['userId']:
            if f['completed']:
                tasks_done += 1
                lists_of_titles.append(f['title'])
    print("Employee {} is done with tasks({}/{}):".
        format(name, tasks_done, total_tasks))
    for title in lists_of_titles:
        print("\t {}".format(title))
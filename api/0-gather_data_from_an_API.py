#!/usr/bin/python3
""" Module """

import json
import requests
from sys import argv, stdout


if __name__ == '__main__':
    """ """
    full_api = requests.get("https://jsonplaceholder.typicode.com/todos/")

    users_api = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}/")

    text_full_api = full_api.text
    text_users_api = users_api.text
    full_data = json.loads(text_full_api)
    users_data = json.loads(text_users_api)

    total_number_of_tasks = 0
    number_of_done_tasks = 0
    completed_task = []

    for todo in full_data:
        if todo['userId'] == users_data['id']:
            if todo['completed']:
                completed_task.append(todo)
                number_of_done_tasks += 1
            total_number_of_tasks += 1

    print(
        f"Employee {users_data['name']} is done with tasks "
        f"({number_of_done_tasks}/{total_number_of_tasks}):")
    for task_title in completed_task:
        print(f"\t {task_title['title']}")

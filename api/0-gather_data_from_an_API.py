#!/usr/bin/python3


"""Script to retrieve employee's TODO list progress"""


import json
import requests
from sys import argv


if __name__ == '__main__':
    # Fetching full TODO list from the API
    full_api = requests.get("https://jsonplaceholder.typicode.com/todos/")
    full_data = full_api.json()

    # Fetching user's information from the API
    user_id = argv[1]
    user_api = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/")
    user_data = user_api.json()

    total_number_of_tasks = 0
    number_of_done_tasks = 0
    completed_task_titles = []

    # Counting completed tasks and collecting their titles
    for todo in full_data:
        if todo['userId'] == int(user_id):
            if todo['completed']:
                completed_task_titles.append(todo['title'])
                number_of_done_tasks += 1
            total_number_of_tasks += 1

    print(
        f"Employee {user_data['name']} is done with tasks "
        f"({number_of_done_tasks}/{total_number_of_tasks}):"
    )
    for title in completed_task_titles:
        print(f"\t{title}")

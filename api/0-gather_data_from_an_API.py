#!/usr/bin/python3
"""document """


import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Returns information about an employee's TODO list progress."""

    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user = response.json()

    response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos = response.json()

    # Calculate progress
    total_tasks = len(todos)
    tasks_done = sum(1 for t in todos if t['completed'])
    titles_done = [t['title'] for t in todos if t['completed']]

    print(
        f"Employee {user['name']} \
        is done with tasks ({tasks_done}/{total_tasks}):")
    for title in titles_done:
        print(f"\t {title}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python api_script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

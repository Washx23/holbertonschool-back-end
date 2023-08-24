#!/usr/bin/python3
""" Documents """

import json
import requests
import sys

if __name__ == '__main__':
    """ """

    full_api = requests.get("https://jsonplaceholder.typicode.com/todos/")
    users_api = requests.get("https://jsonplaceholder.typicode.com/users/")

    text_full_api = full_api.text
    text_users_api = users_api.text
    full_data = json.loads(text_full_api)
    users_data = json.loads(text_users_api)

    user_tasks = {}

    for user in users_data:
        user_id = user['id']
        user_username = user['username']
        user_tasks[user_id] = []

        for task in full_data:
            if task['userId'] == user_id:
                task_data = {
                    "username": user_username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                user_tasks[user_id].append(task_data)

    json_file_name = "todo_all_employees.json"

    with open(json_file_name, 'w') as json_file:
        json.dump(user_tasks, json_file)

    print("Tasks for all employees exported to {}"
          .format(json_file_name), file=sys.stdout)

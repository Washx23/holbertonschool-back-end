#!/usr/bin/python3
""" Documents """

import json
import requests
import sys

if __name__ == '__main__':
    """ """

    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    full_api = requests.get("https://jsonplaceholder.typicode.com/todos/")
    users_api = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id))

    text_full_api = full_api.text
    text_users_api = users_api.text
    full_data = json.loads(text_full_api)
    users_data = json.loads(text_users_api)

    user_tasks = []

    for alls in full_data:
        if alls['userId'] == int(user_id):
            task_data = {
                "task": alls['title'],
                "completed": alls['completed'],
                "username": users_data['username']
            }
            user_tasks.append(task_data)

    json_file_name = "{}.json".format(user_id)

    with open(json_file_name, 'w') as json_file:
        json.dump({users_data['id']: user_tasks}, json_file)

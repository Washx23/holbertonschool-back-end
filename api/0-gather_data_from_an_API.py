#!/usr/bin/python3
""" Documents """

import json
import requests
import sys


if __name__ == '__main__':
    """ """

    full_api = requests.get("https://jsonplaceholder.typicode.com/todos/")

    users_api = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/".format(sys.argv[1]))

    text_full_api = full_api.text
    text_users_api = users_api.text
    full_data = json.loads(text_full_api)
    users_data = json.loads(text_users_api)

    total_task = 0
    done_task = 0
    task_complete = []

    for alls in full_data:
        if alls['userId'] == users_data['id']:
            if alls['completed']:
                task_complete.append(alls)
                done_task += 1
            total_task += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(users_data['name'], done_task, total_task), file=sys.stdout)
    for task_title in task_complete:
        print("\t {}".format(task_title['title']), file=sys.stdout)

#!/usr/bin/python3
""" Documents """

import json
import requests
import sys
import csv

if __name__ == '__main__':
    """ documents """

    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    full_api = requests.get("https://jsonplaceholder.typicode.com/todos/")
    users_api = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(user_id))

    text_full_api = full_api.text
    text_users_api = users_api.text
    full_data = json.loads(text_full_api)
    users_data = json.loads(text_users_api)

    total_task = 0
    done_task = 0
    task_complete = []

    for alls in full_data:
        if alls['userId'] == int(user_id):
            if alls['completed']:
                task_complete.append(alls)
                done_task += 1
            total_task += 1

    csv_file_name = "{}.csv".format(user_id)

    with open(csv_file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task_title in task_complete:
            csv_writer.writerow([str(users_data['id']), users_data['username'], str(task_title['completed']), task_title['title']])

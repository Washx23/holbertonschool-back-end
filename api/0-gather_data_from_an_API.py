import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 todo.py employee_id")
    sys.exit(1)

employee_id = sys.argv[1]
url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

try:
    response_user = requests.get(url_user)
    response_todo = requests.get(url_todo)
    response_user.raise_for_status()
    response_todo.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
    sys.exit(1)

employee_name = response_user.json().get('name')
total_tasks = len(response_todo.json())
completed_tasks = sum(task.get('completed') for task in response_todo.json())
completed_titles = [task.get('title') for task in response_todo.json() if task.get('completed')]

print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
for title in completed_titles:
    print("\t ", title)

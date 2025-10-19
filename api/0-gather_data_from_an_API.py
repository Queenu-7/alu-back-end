#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(url_user)
    todos_response = requests.get(url_todos)

    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)

    user = user_response.json()
    todos = todos_response.json()

    name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    print(f"Employee {name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


#!/usr/bin/python3
"""Gather data from an API and display TODO list progress for a given employee."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    # Fetch user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    employee_name = user_data.get("name")

    # Fetch TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Process tasks
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_done = len(done_tasks)

    # Print first line
    print(f"Employee {employee_name} is done with tasks({number_done}/{total_tasks}):")

    # Print completed tasks with proper formatting
    for task in done_tasks:
        print("\t {}".format(task.get("title")))



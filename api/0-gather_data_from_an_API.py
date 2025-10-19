#!/usr/bin/python3
"""
Script that uses a REST API to return TODO list progress
for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    # Ensure the script receives exactly one integer argument
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Base URLs for user and todos
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user and todos data
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Ensure both requests succeeded
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data from API.")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    # Extract name and task info
    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]

    # Print summary
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")

    # Print completed task titles
    for task in done_tasks:
        print(f"\t {task.get('title')}")

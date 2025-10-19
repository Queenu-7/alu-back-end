#!/usr/bin/python3
"""
This script exports all tasks for a given employee ID to a CSV file.
The output CSV is named USER_ID.csv and contains fields:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user and tasks
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)

    user = user_response.json()
    username = user.get("username")
    todos = todos_response.json()

    # File output
    filename = f"{employee_id}.csv"

    with open(filename, mode="w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])

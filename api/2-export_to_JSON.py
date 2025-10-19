#!/usr/bin/python3
"""
Script that exports data in the JSON format
for a given employee ID.
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # API URLs
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )

    # Fetch user and todos data
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")
    filename = "{}.json".format(employee_id)

    # Build JSON structure
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(employee_id): tasks}

    # Write to file
    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)

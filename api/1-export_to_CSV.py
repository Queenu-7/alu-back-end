#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Base URL
    base_url = "https://jsonplaceholder.typicode.com"

    # Get user info
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get the TODOs for the employee
    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    todos = todos_response.json()

    # Filter completed tasks
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_count = len(done_tasks)

    # Print progress
    print(f"Employee {employee_name} is done with tasks({done_count}/{total_tasks}):")

    # Print each completed task
    for task in done_tasks:
        print(f"\t {task.get('title')}")

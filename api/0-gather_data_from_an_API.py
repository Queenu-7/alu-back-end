#!/usr/bin/python3
"""
Python script that fetches employee TODO list progress from a REST API
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID
    
    Args:
        employee_id (int): The ID of the employee
    """
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee details
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found")
        return
    
    user_data = user_response.json()
    employee_name = user_data.get('name')
    
    # Get TODO list for the employee
    todos_url = f"{base_url}/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error: Could not fetch TODO list for employee {employee_id}")
        return
    
    todos_data = todos_response.json()
    
    # Calculate task statistics
    total_tasks = len(todos_data)
    completed_tasks = 0
    completed_titles = []
    
    for task in todos_data:
        if task.get('completed'):
            completed_tasks += 1
            completed_titles.append(task.get('title'))
    
    # Display the progress
    print(f"Employee {employee_name} is done with "
          f"tasks({completed_tasks}/{total_tasks}):")
    
    # Display completed task titles
    for title in completed_titles:
        print(f"\t {title}")


if __name__ == "__main__":
    # Check if employee ID is provided as command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not connect to API - {e}")
        sys.exit(1)

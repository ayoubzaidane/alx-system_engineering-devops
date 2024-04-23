import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee whose TODO list progress is to be fetched.

    Returns:
        None
    """
    # API URL
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetching TODO data
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print("No TODOs found for this employee.")
        return

    # Extracting employee name
    employee_name = todos[0]['name']

    # Counting completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)

    # Total number of tasks
    total_tasks = len(todos)

    # Displaying progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")

    # Displaying completed tasks titles
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)


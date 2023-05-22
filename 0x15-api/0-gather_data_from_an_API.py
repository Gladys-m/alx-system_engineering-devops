#!/usr/bin/python3
""" Gather data from an API  """

if __name__ == "__main__":
    import requests

    def get_employee_todo_progress(employee_id):
        base_url = "https://jsonplaceholder.typicode.com"
        employee_url = f"{base_url}/users/{employee_id}"
        todos_url = f"{base_url}/todos?userId={employee_id}"

        try:
            # Fetch employee details
            employee_response = requests.get(employee_url)
            employee_response.raise_for_status()
            employee_data = employee_response.json()

            # Fetch employee's TODO list
            todos_response = requests.get(todos_url)
            todos_response.raise_for_status()
            todos_data = todos_response.json()

            # Extract relevant information
            employee_name = employee_data["name"]
            total_tasks = len(todos_data)
            completed_tasks = [todo["title"] for todo in todos_data if todo["completed"]]

            # Display progress information
            print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
            for task in completed_tasks:
                print(f"\t{task}")

            except requests.exceptions.RequestException as e:
                print("Error occurred:", e)

            # Test the function with an employee ID
            employee_id = 1  # Replace with the desired employee ID
            get_employee_todo_progress(employee_id)

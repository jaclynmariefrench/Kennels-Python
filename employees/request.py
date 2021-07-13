EMPLOYEES = [
    {"id": 1, "name": "Jeremy Bakker", "employeeId": 2},
    {"id": 2, "name": "Geneva Direction", "employeeId": 1},
    {"id": 3, "name": "Franklin Moore", "employeeId": 2},
    {"id": 4, "name": "Patrick Streeter", "employeeId": 1},
    {"name": "Jackie West", "employeeId": 1, "id": 5},
]


def get_all_employees():
    """returning the employee dictonaries
    """
    return EMPLOYEES


# Function with a single parameter


def get_single_employee(id):
    """loop over employee dictonaries"""
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the employees list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    """creating new employee"""
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)
    return employee

class Employee:
    """class for new employee dictonary"""

    def __init__(self, id, name, location_id):
        self.id = id
        self.name = name
        self.location_id = location_id


new_employee = Employee(10, "John Smith", 3)

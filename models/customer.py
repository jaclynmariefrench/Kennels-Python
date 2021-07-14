class Customer:
    """class for new customer dictonary"""

    def __init__(self, id, name, address, animal_id, email):
        self.id = id
        self.name = name
        self.address = address
        self.animal_id = animal_id
        self.email = email


new_customer = Customer(
    6, "John Smith", "111 Somewhere Dr.", 2, "johnsmith@kennels.com"
)

class Customer:
    """class for new customer dictonary"""

    def __init__(self, id, name, address, email= "", password= ""):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password


new_customer = Customer(
    6, "John Smith", "111 Somewhere Dr.", 2, "johnsmith@kennels.com"
)

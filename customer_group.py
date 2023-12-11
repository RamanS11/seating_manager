class CustomerGroup:
    """
    A class to represent a customer's group to be seated on the tables
    """
    size: int = None                    # Defines the number of customers within the group
    status: bool = False                # Defines the status of the customer's group (True if seated, False otherwise)

    def __init__(self, size: int = None):
        self.set_size(size=size)

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_status(self):
        return self.status

    def set_status(self, status: bool):
        self.status = status

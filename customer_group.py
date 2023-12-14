import uuid

import config


class CustomerGroup:
    """A class to represent a customer's group to be seated on the tables."""

    size: int = None  # Defines the number of customers within the group
    status: bool = False  # Defines the status of the customer's group (True if seated, False otherwise)
    table_id: uuid = (
        None  # Defines the id of the table that the group is seated (if status is True)
    )

    def __init__(self, size: int = None):
        self.set_size(size=size)

    def get_size(self):
        return self.size

    def set_size(self, size):
        assert (
            size < config.MAX_GROUP_SIZE
        ), f"Group size must be less than {config.MAX_GROUP_SIZE}"
        self.size = size

    def get_status(self):
        return self.status

    def get_table_id(self):
        assert self.status, "Cannot get table_id for CustomerGroup that is not seated!"
        return self.table_id

    def update_status(self, status: bool, table_id: str):
        self.status = status
        self.table_id = table_id

    def restore_status(self):
        self.status = False
        self.table_id = None

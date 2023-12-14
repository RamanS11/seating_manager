import uuid

import config


class Table:
    """Table class that stores information about the chairs."""

    size: int = None  # Defines the amount of chairs around a table
    empty_seats: int = None  # Defines the amount of free seats in the table
    id: uuid = None  # UUID that identifies the table instance.

    def __init__(self, size: int, empty_seats: int):
        """Initialize table with empty seats."""
        self.set_size(size=size)
        self.set_empty_seats(empty_seats=empty_seats)
        self.id = uuid.uuid4().hex

    def get_size(self):
        return self.size

    def set_size(self, size: int):
        assert type(size) is int, "size must be an integer"
        assert (
            2 <= size <= config.MAX_TABLE_SIZE
        ), f"Tables can accommodate between 2 to {config.MAX_TABLE_SIZE} people"
        self.size = size

    def get_empty_seats(self):
        return self.empty_seats

    def set_empty_seats(self, empty_seats: int):
        assert type(empty_seats) is int, "empty_seats must be an integer"
        assert (
            self.size >= empty_seats
        ), "cannot have more empty seats than table's size"
        self.empty_seats = max(0, empty_seats)

    def get_id(self):
        return self.id

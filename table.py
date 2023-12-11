class Table:
    """
    Table class that stores information about the chairs
    """
    size: int = None                        # Defines the amount of chairs around a table
    empty_seats: int = None                 # Defines the amount of free seats in the table
    id: int = None                          # Variable to identify the seats

    def __init__(self, size: int, empty_seats: int, table_id: int):
        """
        Initialize table with empty seats
        """
        self.set_size(size=size)
        self.set_empty_seats(empty_seats=empty_seats)
        self.set_id(table_id=table_id)

    def get_size(self):
        return self.size

    def set_size(self, size: int):
        assert type(size) is int, "size must be an integer"
        assert 2 < size < 6, "Tables can accommodate between 2 to 6 people"
        self.size = size

    def get_empty_seats(self):
        return self.empty_seats

    def set_empty_seats(self, empty_seats: int):
        assert type(empty_seats) is int, "empty_seats must be an integer"
        assert self.size >= empty_seats, "cannot have more empty seats than table's size"
        self.empty_seats = empty_seats

    def set_id(self, table_id: int):
        self.id = table_id

    def get_id(self):
        return self

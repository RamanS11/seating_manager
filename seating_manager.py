from typing import Dict
from typing import List

import config
from customer_group import CustomerGroup
from table import Table


class SeatingManager:
    """The seating manager class is responsible for dealing with the methods
    when a group arrives/leaves a table."""

    tables: Dict[Table.id, Table] = None  # List of tables within the restaurant
    sets: List[
        set
    ] = None  # List of sets containing IDs of different available amount of seats.

    def __init__(self, tables: List[Table]):
        self.tables = {obj.id: obj for obj in tables}
        self.create_sets_of_tables(tables=tables)

    def create_sets_of_tables(self, tables: List[Table]):
        """Function that creates sets having as value the table_id.

        Each of the sets will be used in order to store the id of those
        tables with (0 to 6) available seats.
        """
        free_seats_0 = {t.id for t in tables if t.get_empty_seats() == 0}
        free_seats_1 = {t.id for t in tables if t.get_empty_seats() == 1}
        free_seats_2 = {t.id for t in tables if t.get_empty_seats() == 2}
        free_seats_3 = {t.id for t in tables if t.get_empty_seats() == 3}
        free_seats_4 = {t.id for t in tables if t.get_empty_seats() == 4}
        free_seats_5 = {t.id for t in tables if t.get_empty_seats() == 5}
        free_seats_6 = {t.id for t in tables if t.get_empty_seats() == 6}
        self.sets = [
            free_seats_0,
            free_seats_1,
            free_seats_2,
            free_seats_3,
            free_seats_4,
            free_seats_5,
            free_seats_6,
        ]

    def arrives(self, group: CustomerGroup):
        """
        This method is responsible for dealing with the scenario when a group wants to be seated.
        1rst checks how many seats are needed for the group, after that checks tables with at leas the same amount of
        available seats (if not found, then it looks for seats_needed + 1, until reaching 6).
        Args:
            group: CustomerGroup instance.

        Returns: True if the group is seated, False otherwise.
        """
        # Get amount of empty seats needed to allocate the incoming group.
        seats_needed = group.get_size()

        # Assert that all the data is correct so far.
        assert seats_needed <= config.MAX_TABLE_SIZE, (
            "Number of seats insufficient to accommodate the current \n"
            "Customer group in a single table!. \n"
            "Only can accommodate a maximum of {} seats".format(config.MAX_TABLE_SIZE)
        )

        # Initialize table_id as None, and change to an actual table_id value if found empty seats.
        table_id = None
        # Iterate over the list of sets in order to find available seats that coincides with group size.
        for i in range(seats_needed, config.MAX_TABLE_SIZE):
            current_set = self.sets[i]
            if len(current_set) > 0:
                table_id = current_set.pop()
                table_id_new_set = i - seats_needed
                self.sets[table_id_new_set].add(table_id)
                group.update_status(status=True, table_id=table_id)
                self.tables.get(table_id).set_empty_seats(empty_seats=table_id_new_set)
                return True

        return False

    def leaves(self, group: CustomerGroup):
        """
        This method is responsible for dealing with the scenario when a group leaves a table. First recalls the amount
        of people within the group, search for the table they were seated in, and then free the seats by updating the
        sets accordingly.
        Args:
            group: CustomerGroup instance

        Returns: True if successful, False otherwise
        """
        # Checks amount of seats to be freed, and the table where they were seated
        seats_empty = group.get_size()
        table_id = self.locate(group=group)

        # Assert that info is correct so far
        assert table_id is not None, "The group has not yet been seated."
        assert (
            seats_empty <= config.MAX_GROUP_SIZE
        ), "The group is too large! Error in some operation!"

        # Iterate over the list of sets in order to find the actual amount of free sets.
        for i, iter_set in enumerate(self.sets):
            if table_id in iter_set:
                # Once located, adjust the amount of empty seats for table_id according to the group size.
                table_free_seats = i + seats_empty
                self.sets[i].remove(table_id)
                self.sets[table_free_seats].add(table_id)
                self.tables.get(table_id).set_empty_seats(empty_seats=table_free_seats)
                group.restore_status()
                return True

        return False

    def locate(self, group: CustomerGroup):
        """
        This method returns the table at which the group is seated, or null if they are not seated (waiting for a table
        or if they already left).
        Args:
            group: CustomerGroup instance

        Returns: table_id if group is seated, None otherwise
        """
        if group.status:
            return group.get_table_id()

        return None

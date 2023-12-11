from customer_group import CustomerGroup
from table import Table

from typing import List


class SeatingManager:
    """
    The seating manager class is responsible for dealing with the methods when a group arrives/leaves a table.
    """
    tables: List[Table] = None              # List of tables within the restaurant

    def __init__(self, tables: List[Table]):
        self.table = tables

    def arrives(self, group: CustomerGroup):
        """
        This method is responsible for dealing with the scenario when a group wants to be seated.
        Args:
            group: CustomerGroup instance

        Returns:
        """

    def leaves(self, group: CustomerGroup):
        """
        This method is responsible for dealing with the scenario when a group leaves a table.
        Args:
            group: CustomerGroup instance

        Returns:
        """

    def locate(self, group: CustomerGroup):
        """
        This method returns the table at which the group is seated, or null if they are not seated (waiting for a table
        or if they already left).
        Args:
            group: CustomerGroup instance

        Returns:
        """

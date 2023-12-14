import logging
from typing import List

import numpy as np
import typer
from typing_extensions import Annotated

import config
from customer_group import CustomerGroup
from seating_manager import SeatingManager
from table import Table


app = typer.Typer(
    help="Application in charge of seating the customer groups in their respective tables.",
    add_completion=False,
)


def create_tables(total_tables: int) -> List[Table]:
    """
    Function that creates the different instances of tables depending on user's input.
    Number of chairs per table is created randomly.
    Args:
        total_tables: Integer number of tables to create.

    Returns:
        List[Table]: A list of tables created
    """
    assert type(total_tables) is int, "Total tables must be an integer."

    tables: List[Table] = []
    for i in range(total_tables):
        num_chairs = int(np.random.randint(low=2, high=config.MAX_TABLE_SIZE))
        tables.append(Table(size=num_chairs, empty_seats=num_chairs))
    return tables


def create_groups(total_groups: int) -> List[CustomerGroup]:
    """
    Function that creates the different instances of groups depending on user's input.
    Number of members per group is created randomly.
    Args:
        total_groups: Int: Total number of groups

    Returns: List[CustomerGroup]: A list with all groups created.
    """
    assert type(total_groups) is int, "Total tables must be an integer."

    groups: List[CustomerGroup] = []
    for i in range(total_groups):
        num_members = int(np.random.randint(low=2, high=config.MAX_GROUP_SIZE))
        groups.append(CustomerGroup(size=num_members))
    return groups


@app.command()
def main(
    total_tables: Annotated[
        int,
        typer.Option(
            help="Total number of tables to be handled by the seating manager."
        ),
    ] = 1234124,
    total_groups: Annotated[
        int,
        typer.Option(
            help="Total number of groups to be handled by the seating manager."
        ),
    ] = 1000000,
):
    # Creates all tables.
    logging.info(f"Total number of tables: {total_tables}")
    tables = create_tables(total_tables=total_tables)

    # Creates all groups.
    logging.info(f"Total number of groups: {total_groups}")
    groups = create_groups(total_groups=total_groups)

    # Initialize seating manager:
    seating_manager = SeatingManager(tables=tables)

    logging.info("Starting seating manager (Arrive method)")
    for g in groups:
        seating_manager.arrives(group=g)

    logging.info("Starting seating manager (Leave method)")
    not_Seat = 0
    for g in groups:
        try:
            seating_manager.leaves(group=g)
        except AssertionError as e:
            logging.error(e)
            not_Seat += 1
    print(not_Seat)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )

    app()

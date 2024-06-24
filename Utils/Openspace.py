import random
from typing import List
import pandas as pd

from Utils.People import People
from Utils.Table import Table
from Utils.Config import Config


class Openspace:
    def __init__(self, config):
        """
        Initializes an Openspace with a specified capacity.

        Args:
            nbCapacity (int): The maximum capacity of the openspace. Default is 24.
        """
        self.config = config
        self.nbCapacity = self.config.getConfig['limitTable'] * self.config.getConfig['capacity']
        self.openspace = []

    @property
    def getNbCapacity(self) -> int:
        """
        Returns the maximum capacity of the openspace.

        Returns:
            int: Maximum capacity of the openspace.
        """
        return self.nbCapacity

    def setNbCapacity(self, nbMax: int) -> None:
        """
        Change the number of nbCapacity.
        """
        self.nbCapacity = nbMax

    def organised(self, listName: List[People]) -> None:
        """
        Organizes people into tables in the openspace.

        Args:
            listName (List[People]): List of people names.
        """
        # Shuffle the list of names
        random.shuffle(listName)

        # Initialize all tables
        num_tables = self.config.getConfig['limitTable']
        self.openspace = [Table(self.config) for _ in range(num_tables)]

        # Distribute people across tables in a round-robin manner
        table_index = 0
        unseated_people = []

        for person in listName:
            while self.openspace[table_index].getLeftCapacity <= 0:
                table_index = (table_index + 1) % num_tables
                if all(table.getLeftCapacity <= 0 for table in self.openspace):
                    # All tables are full, add to unseated_people
                    unseated_people.append(person)
                    break
            else:
                self.openspace[table_index].assignSeat(person)
                table_index = (table_index + 1) % num_tables

        # Fill remaining seats with None (empty seats)
        for table in self.openspace:
            while table.getLeftCapacity > 0:
                table.assignSeat(None)

        if unseated_people:
            print("==============\n"
                  "These people could not be seated due to capacity limits:")
            for person in unseated_people:
                print(person.getName)
            print("==============")

    def addOpenspace(self, table: Table) -> None:
        """
        Adds a table to the openspace.

        Args:
            table (Table): The table to add to the openspace.
        """
        self.openspace.append(table)

    def store(self, filename: str) -> None:
        """
        Stores the organization of the openspace into an Excel file.

        Args:
            filename (str): The name of the Excel file where the data will be stored.
        """
        data = []
        for table in self.openspace:
            table_data = [seat.getOccupant.getName if seat.getOccupant else "" for seat in table.getSeats]
            data.append(table_data)

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Write to an Excel file
        df.to_excel(filename, index=False, header=False)

    def display(self) -> None:
        """
            Affiche l'openspace
        """
        for index, table in enumerate(self.openspace, start=1):
            print(f"Table {index}")
            for seat_index, seat in enumerate(table.seats, start=1):
                if seat.getOccupant:
                    print(f"  Seat {seat_index}: Occupied by {seat.getOccupant.getName}")
                else:
                    print(f"  Seat {seat_index}: Free")
            print()

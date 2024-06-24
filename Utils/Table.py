import copy

from typing import List

class Seat:
    """
      A class to represent a seat
      Parameters:
      free (bool): A boolean to register is the seat is free or not. Default to True
      occupant (str) : Register the name of the person sitting in the seat.
      """

    def __init__(self):
        self.occupant: str = ""
        self.free: bool = True

    def __str__(self):
        if self.free:
            return "Free"
        else:
            return f"Occupied by {self.getOccupant}"


    def setOccupant(self, name: str) -> bool:
        """
        Sit a person passed by name in the seat
        bool: True if the person is correctly seated. False otherwise.
        """
        if self.free:
            self.occupant = name
            self.free = False
            return True
        else:
            return False

    def removeOccupant(self) -> str:
        """
        Remove the person from the seat and return the name.
        Returns:
        str : The name of the person who was sitting.
        """
        name = self.occupant
        self.occupant = ""
        self.free = True
        return name
    
    @property
    def getOccupant(self) -> str:
        return self.occupant


class Table:
    """
    A class to represent a table in the openspace with a fixed capacity and seats.
    Attributes:
    capacity (int): The maximum number of seats at the table.
    seats (List[Seat]): The list of seats at the table.
    """

    def __init__(self, config):
        self.capacity = config.getConfig['capacity']
        self.seats: List[Seat] = [Seat() for _ in range(self.capacity)]

    def __str__(self):
        seat_status = ', '.join(str(seat) for seat in self.seats)
        return f"Table capacity: {self.capacity}\n\tSeats: [{seat_status}]"


    def hasFreeSpot(self) -> bool:
        """
        Check if there is at least one free spot at the table.
        Returns:
        bool: True if there is a free spot, False otherwise.
        """
        return any(seat.free for seat in self.seats)

    def assignSeat(self, name) -> bool:
        """
       Assign a seat to a person if a free spot is available.
       Parameters:
       name (str): The name of the person to assign to a seat.
       Returns:
       bool: True if the seat was assigned, False if no free spots are available.
       """
        for seat in self.seats:
            if seat.free:
                seat.setOccupant(name)
                return True
        return False

    @property
    def getLeftCapacity(self) -> int:
        """
        Calculate the number of free spots left at the table.
        Returns:
        int: The number of free spots left.
        """
        return sum(1 for seat in self.seats if seat.free)

    @property
    def getCapacity(self) -> int:
        """
        Returns:
        int: The number of spots.
        """
        return self.capacity
    
    def setCapacity(self, nbMax:int) -> None:
        """
            Change the number of spots.
        """
        self.capacity = nbMax
    
    @property
    def getSeats(self) -> List[Seat]:
        return copy.deepcopy(self.seats)
      
      
import pandas as pd
from Utils.People import People
from Utils.Openspace import Openspace
from copy import deepcopy

# Factory class to manage people
class Factory:
    def __init__(self):
        """
        Initialize a Factory object with an empty list to store Person objects.
        """
        self._peopleList = []

    @property
    def getPeopleList(self):
        """
        Property to return a deep copy of the list of Person objects.

        Returns:
        - list: A deep copy of the list containing Person objects.
        """
        return deepcopy(self._peopleList)

    def addPerson(self, person: People):
        """
        Add a Person object to the factory's list of people.

        Args:
        - person (Person): A Person object to be added to the list.

        Raises:
        - ValueError: If the input is not an instance of Person.
        """
        if isinstance(person, People):
            self._peopleList.append(person)
        else:
            raise ValueError("Only instances of Person can be added to the list")

    def loadPeopleFromExcel(self, file_path: str, openspace: Openspace):
        """
        Load people from an Excel file into the factory.

        Args:
        - file_path (str): Path to the Excel file containing names under 'Colleagues' column.

        Raises:
        - ValueError: If the 'Colleagues' column is not found in the Excel file.
        - FileNotFoundError: If the specified file_path does not exist.
        """
        try:
            df = pd.read_excel(file_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_path}' not found")
        
        if 'Colleagues' in df.columns:
            for _, row in df.iterrows():
                person = People(name=row['Colleagues'])
                self.addPerson(person)
        else:
            raise ValueError("Column 'Colleagues' not found in the Excel file")
        
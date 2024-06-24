class People:
    """
    This class is the representation of a Person.
    """

    def __init__(self, name: str):
        """
        Constructor of the class People.py

        Parameters
        ----------
        name : str
            Name of the person.
        """
        self.name = name  # the name of the People
    
    def __str__(self):
        return self.name

    @property
    def getName(self) -> str:
        """
        Return the name of the People.py.
        """
        return self.name
    
    def setName(self, name:str):
        """
        Set the name of the People.py.
        """
        self.name = name

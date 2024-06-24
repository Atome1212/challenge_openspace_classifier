# Openspace Organizer

## Project Description

The Openspace Organizer project is designed to manage seating arrangements in a new office open space. The primary objective is to randomly assign colleagues to different spots each day, promoting interaction and helping team members get to know each other better. The open space consists of 6 tables, each with 4 seats.

![Musical Chairs!](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXk0dmRlMmJwdnF2M3o4Zm1lMThxMGJ3NW50YXp0aTJnbmowbXloZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/z58mi6WUDTXUoFECTm/giphy.webp)

## Mission Objectives

- Develop an algorithm to randomly assign seats to people in the open space.
- Utilize Object-Oriented Programming (OOP) principles.
- Maintain a clean project architecture with proper use of imports.
- Read data from an XLS file for seating assignments.
- Collaboratively use Git and Trello for task management, branching, and pull requests.

## Learning Objectives

- Implement and utilize classes effectively.
- Structure a project cleanly and logically.
- Employ Git for version control and collaborative development.

## Project Details

### Algorithm

The algorithm implemented in this project randomly assigns people to seats in the open space. The algorithm ensures that each person gets to sit with different colleagues each day to promote interaction. The seating arrangement is stored and can be read from and written to an XLS file.

### Classes and Modules

The project is divided into several modules, each handling a specific part of the functionality:

- **Factory.py**: This module contains the `Factory` class responsible for creating instances of various objects used in the project, such as `Person`, `Table`, and `Openspace`.
     ```python
    class Factory:
        @staticmethod
        def create_person(name):
            return Person(name)
        
        @staticmethod
        def create_table(table_number):
            return Table(table_number)
        
        @staticmethod
        def create_openspace(tables):
            return Openspace(tables)

- **Openspace.py**: This module defines the `Openspace` class, which represents the entire seating area. It includes methods to manage the overall seating arrangement.
    ```python
    class Openspace:
        def __init__(self, tables):
            self.tables = tables
        
        def assign_seats(self, people):
            # Algorithm to randomly assign people to seats
            pass

- **People.py**: This module defines the `Person` class, representing individuals who will be seated in the open space.
    ```python
    class Person:
    def __init__(self, name):
        self.name = name

- **Table.py**: This module defines the `Table` class, which represents a table in the open space and manages the seating at that table.
    ```python
    class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.seats = []
    
    def add_person(self, person):
        if len(self.seats) < 4:
            self.seats.append(person)


### Project Structure

```plaintext
challenge-openspace-classifier/
├── .git/
│   ├── [git internals and hooks]
├── Utils/
│   ├── __init__.py
│   ├── Factory.py
│   ├── Openspace.py
│   ├── People.py
│   └── Table.py
├── .gitignore
├── main.py
└── README.md
```
### Conclusion
The Openspace Organizer project provides a practical solution to managing dynamic seating arrangements in an open office environment. By leveraging OOP principles and a clean project architecture, it ensures that colleagues interact with different people each day, fostering a collaborative and engaging workplace culture. The project also demonstrates effective use of Git for version control and team collaboration, making it an excellent example of modern software development practices.

With the flexibility to read and write seating data from an XLS file, the project is both user-friendly and adaptable to different office setups. Contributions to the project are welcome, and we encourage developers to get involved and help improve the functionality and features of the Openspace Organizer.

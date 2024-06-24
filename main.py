import os
import platform

from Utils.Config import Config
from Utils.Factory import Factory
from Utils.Openspace import Openspace


def main():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system("clear")

    print("""
+-------------------+
|       Hello!      |
+-------------------+""")

    choice = '0'
    facto = None
    openspace = None

    while choice != '9':
        choice = input("""
1. Shuffle people around
2. Check how many seats
3. Check how many people
4. Check how many free spots
9. Exit
Enter your choice : """)

        match choice:
            case '1':
                print("Shuffling people around...\n")
                config = Config()
                config.loadOrCreateConfig()
                facto = Factory()
                openspace = Openspace(config)

                facto.loadPeopleFromExcel("./Data/Example_Excel_Template.xlsx", openspace)
                openspace.organised(facto.getPeopleList)
                openspace.store("./Data/ordered.xlsx")
                openspace.display()
            case '2':
                if openspace:
                    print(f"There are {openspace.getNbCapacity} seats in this openspace")
                else:
                    print("Openspace not initialized. Please select option 1 first.")
            case '3':
                if openspace:
                    print(f"There is {len(facto.getPeopleList)} people in this openspace")
                else:
                    print("Openspace not initialized. Please select option 1 first.")
            case '4':
                if openspace:
                    print(f"There is {openspace.getNbCapacity - len(facto.getPeopleList)} free seats in this openspace")
                else:
                    print("Openspace not initialized. Please select option 1 first.")
            case '9':
                print("Okay bye")
            case _:
                print("Invalid choice, please try again.")

        print("+--------------------------------------------+")


if __name__ == "__main__":
    main()

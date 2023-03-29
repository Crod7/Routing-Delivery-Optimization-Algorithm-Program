import HashTable
from Truck import Truck
from LoadPackageData import loadPackageData
from Gui import mainMenu
from OrganizeTruckLoad import organize


# This function will run the entire program as an instance. As to not cause any errors or glithces
# from running multiple calls to the database, the run function resets the data in the Hash Table and
# the truck objects. This makes the data accurate and not stack on top of each other.
def run():
    database = HashTable.HashChain(10)                  # This empty Hash Table will hold all package data.

    loadPackageData("WGUPS Package File.csv", database) # This will load the Hash Table with all the package data.

    truck1 = Truck(18, 0, "HUB", [], None, 0)           # We make 3 Truck objects to deliver all the packages.
    truck2 = Truck(18, 0, "HUB", [], None, 0)
    truck3 = Truck(18, 0, "HUB", [], None, 0)

    organize(truck1, truck2, truck3, database)          # We use this function to organize how all the packages will be
                                                        #   loaded into their respective Trucks and from what database.
                                                        #   In this case we use the three Truck objects and our
                                                        #   database Hash Table.

    mainMenu(truck1, truck2, truck3, database)          # This handles the Main Menu, allows the user to make a 
                                                        #   a selection to get a report based on desired data.



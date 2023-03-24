import csv
import Dijkstra
import HashTable
from Truck import Truck
from Graph import Graph,Vertex
from LoadPackageData import loadPackageData
from LoadDistanceData import loadDistanceData


database = HashTable.HashChain(10)

loadPackageData("WGUPS Package File.csv", database)


truck1 = Truck(18,0," 6351 South 900 East\n(84121)", [], None, 0)
truck2 = Truck(18, 0, " HUB", [], None, 0)
truck3 = Truck(18, 0, " HUB", [], None, 0)

#Turck leaving right away
truck1.loadPackage(database.search(1))
truck1.loadPackage(database.search(2))
truck1.loadPackage(database.search(4))
truck1.loadPackage(database.search(5))
truck1.loadPackage(database.search(7))
truck1.loadPackage(database.search(27))
truck1.loadPackage(database.search(10))
truck1.loadPackage(database.search(11))
truck1.loadPackage(database.search(12))
truck2.loadPackage(database.search(29))
truck2.loadPackage(database.search(30))
truck2.loadPackage(database.search(33))
truck2.loadPackage(database.search(34))
truck2.loadPackage(database.search(35))
truck2.loadPackage(database.search(40))
#must leave at 9:05
truck2.loadPackage(database.search(3))
truck2.loadPackage(database.search(39))
truck2.loadPackage(database.search(13))
truck2.loadPackage(database.search(14))
truck2.loadPackage(database.search(15))
truck2.loadPackage(database.search(16))
truck2.loadPackage(database.search(17))
truck2.loadPackage(database.search(18))
truck2.loadPackage(database.search(19))
truck2.loadPackage(database.search(20))
truck2.loadPackage(database.search(21))
truck2.loadPackage(database.search(31))
truck2.loadPackage(database.search(32))
truck2.loadPackage(database.search(37))
truck2.loadPackage(database.search(36))
truck2.loadPackage(database.search(38))
#Last truck to go out
truck3.loadPackage(database.search(8))
truck3.loadPackage(database.search(9))
truck3.loadPackage(database.search(25))
truck3.loadPackage(database.search(26))
truck3.loadPackage(database.search(22))
truck3.loadPackage(database.search(23))
truck3.loadPackage(database.search(24))
truck3.loadPackage(database.search(28))
truck3.loadPackage(database.search(6))

###########################################################

firstColumn = []
with open("WGUPS Distance Table.csv") as distanceCsv:
    distanceData = csv.reader(distanceCsv, delimiter=',')
    for distance in distanceData:
        firstColumn.append(distance)


i = 0
while i < len(truck1.packages):
    print("======================================= Package " + str(i) + " Summary =======================================")
        #This compares the inside of each array with a given address
    countRow = 0
    start = 0 #We set the start at 0 because 0 is where the HUB is. The program won't find HUB in the for loop
            #but will still calculate it correctly.
    end = 2   #We need to make this 2 to skip the first column in the csv file.
    if i != 0:
        truck1.currentLocation = truck1.packages[i - 1].address
    else:
        truck1.currentLocation = 'HUB'
    truck1.nextLocation = truck1.packages[i].address
    print("Current Location: " + truck1.currentLocation)
    print("Next    Location: " + truck1.nextLocation)

    for address in firstColumn: # The entire row ['name + address', 'address', distance, distance, ...]
                                # address[1] is the delivery address that should be checked
        if truck1.currentLocation == address[1][1: -8]: #If the current trucks address is equal to this other address
            start = countRow
            print("start found " + str(countRow))
        if truck1.nextLocation == address[1][1: -8]:
            end = countRow
            print("end found " + str(countRow))
        countRow = countRow + 1

    try:
        if firstColumn[start][end] != '':           # If distance is found, set this as the distance
            distance = firstColumn[start][end]
        else:                                       # If no distance found, reversing the matrix gives distance
            distance = firstColumn[end][start + 2]
        
        newMilage = float(distance)                 # Convert the distance to a float to add to truck
    except:
        if firstColumn[end][start] != '':           # If distance is found, set this as the distance
            distance = firstColumn[start][end+1]
        else:                                       # If no distance found, reversing the matrix gives distance
            distance = firstColumn[end][start + 2]
        
        newMilage = float(distance) 
    
    truck1.milage += newMilage                  # Truck's new milage is calculated

    print("new milage added: "+ str(newMilage))
    i += 1
    print("total milage    :  " + str(truck1.milage))

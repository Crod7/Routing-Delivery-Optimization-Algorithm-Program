import csv
import Dijkstra
import HashTable
from Truck import Truck
from Graph import Graph,Vertex
from LoadPackageData import loadPackageData
from LoadDistanceData import loadDistanceData


database = HashTable.HashChain(10)

loadPackageData("WGUPS Package File.csv", database)


truck1 = Truck(18,0,"HUB", [], None, 0)
truck2 = Truck(18, 0, "HUB", [], None, 0)
truck3 = Truck(18, 0, "HUB", [], None, 0)

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

#loadDistanceData("WGUPS Distance Table.csv", truck1.currentLocation, truck1.nextLocation)
#for i in range(len(database.table)+1):
#    print("Package: {}".format(database.search(i+1)))

#Create the vertexes

firstColumn = []
with open("WGUPS Distance Table.csv") as distanceCsv:
    distanceData = csv.reader(distanceCsv, delimiter=',')
    #next(distanceData) # skips header
    for distance in distanceData:
        firstColumn.append(distance)

print(firstColumn[0][1])
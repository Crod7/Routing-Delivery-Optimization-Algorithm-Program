import csv
import Dijkstra
import HashTable
from Truck import Truck
from Graph import Graph,Vertex
from LoadPackageData import loadPackageData
from LoadDistanceData import loadDistanceData
from DeliverPackages import truckRun


database = HashTable.HashChain(10)

loadPackageData("WGUPS Package File.csv", database)


truck1 = Truck(18, 0, "HUB", [], None, 0)
truck2 = Truck(18, 0, "HUB", [], None, 0)
truck3 = Truck(18, 0, "HUB", [], None, 0)

#Truck leaving right away
truck1.loadPackage(database.search(14))
truck1.loadPackage(database.search(15))
truck1.loadPackage(database.search(19))
truck1.loadPackage(database.search(1))
truck1.loadPackage(database.search(13))
truck1.loadPackage(database.search(16))
truck1.loadPackage(database.search(20))
truck1.loadPackage(database.search(29))
truck1.loadPackage(database.search(30))
truck1.loadPackage(database.search(34))
truck1.loadPackage(database.search(40))
truck2.loadPackage(database.search(2))
truck2.loadPackage(database.search(4))
truck2.loadPackage(database.search(5))
truck2.loadPackage(database.search(7))
truck1.loadPackage(database.search(8))
#must leave at 9:05
truck2.loadPackage(database.search(6))
truck2.loadPackage(database.search(18))
truck2.loadPackage(database.search(25))
truck2.loadPackage(database.search(28))
truck2.loadPackage(database.search(31))
truck2.loadPackage(database.search(32))
truck2.loadPackage(database.search(36))
truck2.loadPackage(database.search(37))
truck2.loadPackage(database.search(38))
truck2.loadPackage(database.search(3))
truck2.loadPackage(database.search(10))
truck2.loadPackage(database.search(11))
truck2.loadPackage(database.search(12))
truck2.loadPackage(database.search(17))
truck2.loadPackage(database.search(21))
truck2.loadPackage(database.search(22))

#Last truck to go out at 10:20am

truck3.loadPackage(database.search(9)) # This is the corrected address, because it is now 10:20am
truck3.loadPackage(database.search(23))
truck3.loadPackage(database.search(24))
truck3.loadPackage(database.search(26))
truck3.loadPackage(database.search(27))
truck3.loadPackage(database.search(33))
truck3.loadPackage(database.search(35))
truck3.loadPackage(database.search(39))

###############################################################################

truckRun(truck1, 0)
#must leave at 9:05
truckRun(truck2, 0)
#must leave at 10:20 and after one of the first trucks has returned
truckRun(truck3, 0)
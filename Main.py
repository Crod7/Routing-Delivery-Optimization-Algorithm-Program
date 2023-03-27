import Dijkstra
import HashTable
from Truck import Truck
from Graph import Graph,Vertex
from LoadPackageData import loadPackageData
from DeliverPackages import truckRun
from Time import timeConvertToInt, intConvertToTime


database = HashTable.HashChain(10)

loadPackageData("WGUPS Package File.csv", database)


truck1 = Truck(18, 0, "HUB", [], None, 0)
truck2 = Truck(18, 0, "HUB", [], None, 0)
truck3 = Truck(18, 0, "HUB", [], None, 0)

# Truck leaving right away at 8:00am
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
truck1.loadPackage(database.search(2))
truck1.loadPackage(database.search(4))
truck1.loadPackage(database.search(5))
truck1.loadPackage(database.search(7))
truck1.loadPackage(database.search(8))
# must leave at 9:05 to allow for delayed packages to arrive
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

#Last truck to go out at 10:20am to allow for package #9 to correct it's address
truck3.loadPackage(database.search(9)) # This is the corrected address, because it is now 10:20am
truck3.loadPackage(database.search(23))
truck3.loadPackage(database.search(24))
truck3.loadPackage(database.search(26))
truck3.loadPackage(database.search(27))
truck3.loadPackage(database.search(33))
truck3.loadPackage(database.search(35))
truck3.loadPackage(database.search(39))

###############################################################################

# The truckRun() function takes a Truck Object and begins it's route to deliver all packages using
# the greedy algorithm.
reportTime = 12
#   name(TruckObject, starting milage, database, startingTime, reportCheck, reportTime, isCheckingReportTime, isThisFinalTruck)
truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'n')       
truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'y'                 , 'n')       
truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'y'                 , 'y')       

# The first Truck leaves at 8:00am
# The second Truck leaves at 9:05am
# The final Truck leaves at 10:20am

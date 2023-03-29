import csv
from Package import Package


# We take thisDatabase and use it's insert method to add new package objects directly from the csv file.
def loadPackageData(filename, thisDatabase):
    with open(filename) as packageCsv:
        packageData = csv.reader(packageCsv, delimiter=',')
        #next(packageData) # skips header
        for package in packageData:
            id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipCode = package[4]
            deadline = package[5]
            weight = package[6]
            deliveryStatus = "at the hub"

            newPackage = Package(id, address, city, state, zipCode, deadline, deliveryStatus, weight)

            thisDatabase.insert(id, newPackage)
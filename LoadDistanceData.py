import csv
from Package import Package

def loadDistanceData(filename, truckStartPos, truckEndPos):
    count = 0
    firstColumn = []
    with open(filename) as distanceCsv:
        distanceData = csv.reader(distanceCsv, delimiter=',')
        next(distanceData) # skips header
        for distance in distanceData:
            firstColumn.append(distance)
    print(firstColumn)
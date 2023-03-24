
class Truck:
    def __init__(self, speed, milage, currentLocation, packages, nextLocation, currentPackage):
        self.speed = speed
        self.milage = milage
        self.currentLocation = currentLocation
        self.packages = []
        self.currentPackage = 0
        self.nextLocation = ''
    
    def nextLocationFunc(self, curr):
        result = self.packages[curr]
        print(result)
        self.currentPackage = self.currentPackage + 1

    def loadPackage(self, package):
        self.packages.append(package)

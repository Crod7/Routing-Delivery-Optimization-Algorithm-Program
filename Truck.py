
class Truck:
    def __init__(self, speed, milage, currentLocation, packages):
        self.speed = speed
        self.milage = milage
        self.currentLocation = currentLocation
        self.packages = []
    
    def loadPackage(self, package):
        self.packages.append(package)
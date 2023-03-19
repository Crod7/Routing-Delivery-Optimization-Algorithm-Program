import csv


# Chaining Hash Table ##################################################################
                
# Package Object #########################################################################
class Package:
    def __init__(self, id, address, city, state, zipCode, deadline, deliveryStatus, weight):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.deliveryStatus = deliveryStatus
        self.state = state
        self.city = city
        self.zipCode = zipCode
        self.weight = weight

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" %(self.id, self.address, self.city, self.state, self.zipCode, self.zipCode, self.deadline, self.deliveryStatus, self.weight)


# Load CSV to Hash Table ##########################################################################

def loadPackageData(filename):
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
            deliveryStatus = "Loaded"

            newPackage = Package(id, address, city, state, zipCode, deadline, deliveryStatus, weight)

            database.insert(id, newPackage)
# Truck Class ############################################################################################
class Truck:
    def __init__(self, speed, milage, currentLocation, packages):
        self.speed = speed
        self.milage = milage
        self.currentLocation = currentLocation
        self.packages = []
    
    def loadPackage(self, package):
        self.packages.append(package)



# Main Function############################################################################################
import HashTable
database = HashTable.HashChain(10)
loadPackageData("WGUPS Package File.csv")
truck1 = Truck(18,0,"hub", [])
truck2 = Truck(18, 0, "hub", [])
truck3 = Truck(18, 0, "hub", [])

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

for i in range(len(database.table)+1):
    print("Package: {}".format(database.search(i+1)))

# Dijkstra Shortest Path #######################################################
class Vertex:
    def __init__(self, label):
        self.label = label

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}
        
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)


def dijkstra_short_path(g, start_vertex):
    unvisited_queue = []
    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)
    start_vertex.distance = 0
    while len(unvisited_queue) > 0:
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)
        #check potential path lengths from the current vertext to all neighbors
        for adj_vertex in g.adjacency_list[current_vertex]:
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = current_vertex.distance + edge_weight

            #if shorter path from start_vertex to add_vertex is found,
            #update adj_vertex's distance and predecessor

            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex

def get_shortest_path(start_vertex, end_vertex):
    path = ' '
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = '->' + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path
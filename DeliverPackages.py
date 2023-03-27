import csv
from Time import timeConvertToInt, intConvertToTime



# truckRun() is a recursive function that delivers all the packages inside a Truck object's load.
def truckRun(truck, isFirstDropOff, database, time):    # We start by placing a Truck object into the function argument.
                                                        # isFirstDropOff lets the program know that the truck should
                                                        #   should start at the Hub and begin delivering from there.
                                                        # database will allow the Truck to mark the packages inside
                                                        #   the database as either 'en route' or 'delivered'.
                                                        # time will help with printing reports on package
                                                        #   delivery status.
                                            

    nearestNeighbor = []                                # This creates a temp list of current distances available to Truck
    
    nearestPackage = []                                 # This creates a temp list of packages still on Truck
    
    database
    
    i = 0                                               # i represents the current package. It will later
                                                        #   be used to iterate through the remaining packages
                                                        #   waiting to be dropped off.

    firstColumn = []                                    # firstColumn represents the distance table and is used
                                                        #   for getting the distance between two addresses.
                                                        #   Each item in the list holds one row from the
                                                        #   distance table.
    
    with open("WGUPS Distance Table.csv") as distanceCsv:   # This will fill the firstColumn[] list.
        distanceData = csv.reader(distanceCsv, delimiter=',')
        for distance in distanceData:
            firstColumn.append(distance)




    # This while loop will iterate through the remaining packages of the Truck.
    # Then after the while loop is complete, the program will have a list of all distances availble to the Truck
    # based on current location. This is what fills the nearestNeighbor[] and nearestPackage[] lists.
    while i < len(truck.packages):
            #This compares the inside of each array with a given address
        countRow = 0
        start = 0 #We set the start at 0 because 0 is where the HUB is. The program won't find HUB in the for loop
                #but will still calculate it correctly.
        end = 2   #We need to make this 2 to skip the first column in the csv file.
        if isFirstDropOff == 0:
            truck.currentLocation = 'HUB' #truck.packages[i - 1].address
        
        truck.nextLocation = truck.packages[i].address
        #print("Current Location: " + truck.currentLocation)
        #print("Next    Location: " + truck.nextLocation)

        for address in firstColumn: # The entire row ['name + address', 'address', distance, distance, ...]
                                    # address[1] is the delivery address that should be checked
            if truck.currentLocation == address[1][1: -8]: #If the current trucks address is equal to this other address
                start = countRow
                #print("start found " + str(countRow))
            if truck.nextLocation == address[1][1: -8]:
                end = countRow
                #print("end found " + str(countRow))
            countRow = countRow + 1


        # This determines the miles between all package locations and the current location
        # It will add all these distances to a list
        try:
            if firstColumn[start][end] != '':           # If distance is found, set this as the distance
                if start >= end:
                    distance = firstColumn[start][end + 2]
                    #print("start > end in try 1") DEBUGGING TOOL
                    #print("CELL: [S,E] : ["+str(start+9)+"]["+str(end + 2)+ "]") DEBUGGING TOOL
                else:                                   # If firstColumn[start][end] is null, reverseing the matrix gives distance
                    distance = firstColumn[end][start + 2]
                    #print("end > start in try 1") DEBUGGING TOOL
                    #print("CELL: [E,S] : ["+str(end+9)+"]["+str(start + 2)+ "]") DEBUGGING TOOL
            else:                                       # If no distance found, reversing the matrix gives distance
                distance = firstColumn[end][start + 2]
                #print("end > start in try 2") DEBUGGING TOOL
                #print("CELL: [E,S] : ["+str(end+9)+"]["+str(start + 2)+ "]") DEBUGGING TOOL
            
            newMilage = float(distance)                 # Convert the distance to a float to add to nearestNeighbor[]
        except:
            if firstColumn[end][start] != '':           # If distance is found, set this as the distance
                distance = firstColumn[start][end+2]
                #print("except1")
            else:                                       # If firstColumn[start][end] is null, reverseing the matrix gives distance
                distance = firstColumn[end][start + 2]
                #print("except2")
            
            newMilage = float(distance)                 # Convert the distance to a float to add to nearestNeighbor[]
        
        # Now we add the distance collected from this package route to a temporary database
        nearestNeighbor.append(newMilage)
        nearestPackage.append(truck.packages[i]) # This is used later to mark and remove package data.
        i += 1                                   # This stops the while loop once every package
                                                 #     has been delivered.



    # If Truck object still has packages remaining, we run this code and call truckRun() again.
    if len(truck.packages) > 0:
        min_value = min(nearestNeighbor)
        smallest_index = nearestNeighbor.index(min_value)
        truck.nextLocation = truck.packages[smallest_index].address

        # This handles the time the package was delivered, and what appears on reports based on time
        timeElapsed = min_value/truck.speed # Trucks traveling at 18 units per hour that have traveled
                                            #   6 units means that 20 minutes have passed,
                                            #   6/18 = 1/3, 1/3 of an hour is 20 minutes.
                                            #   This is how we will include time on our deliveries.
        
        time += timeElapsed           # We add the time that has elapsed to the Trucks current time.
                                            #   This is repeated for every package.

        #print(truck.currentLocation + " ---> " + truck.nextLocation)
        #print(nearestNeighbor)

        truck.milage += min_value
        truck.currentLocation = truck.packages[smallest_index].address
        
        
        curr = truck.packages[smallest_index]           # curr represents the current package being dropped off.
        curr.deliveryStatus = 'delivered at ' + str(intConvertToTime(time))# The status is changed to delivered.
        database.insert(curr.id, curr)                  # The new status is now inserted back into the database.
        
        
        print(curr.deliveryStatus + " Package ID: " + str(curr.id)) # This will print the package's time delivered 

        truck.packages.pop(smallest_index)              # Removes the package from the Trucks load.

        isFirstDropOff = 1                              # Lets the program know that the Truck is no longer
                                                        #   at the HUB.

        truckRun(truck, isFirstDropOff, database, time) # A recursive function that will keep calling itself
                                                        #   until all packages are delivered.
    
    # If no more packages remain on the Truck, we return the total milage driven by this Truck.
    else:
        print("total miles: " + str(truck.milage))

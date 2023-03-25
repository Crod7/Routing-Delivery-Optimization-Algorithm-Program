import csv



#We start by placing a truck object into the function argument.
def truckRun(truck, isFirstDropOff):

    nearestNeighbor = []
    nearestPackage = []
    i = 0
    firstColumn = []
    with open("WGUPS Distance Table.csv") as distanceCsv:
        distanceData = csv.reader(distanceCsv, delimiter=',')
        for distance in distanceData:
            firstColumn.append(distance)

    #print("number of packages in truck: " + str(len(truck.packages)))

    while i < len(truck.packages):
        #print("=== Package " + str(i) + " Summary ==================")
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
                    #print("start > end in try 1")
                    #print("CELL: [S,E] : ["+str(start+9)+"]["+str(end + 2)+ "]")
                else:
                    distance = firstColumn[end][start + 2]
                    #print("end > start in try 1")
                    #print("CELL: [E,S] : ["+str(end+9)+"]["+str(start + 2)+ "]")
            else:                                       # If no distance found, reversing the matrix gives distance
                distance = firstColumn[end][start + 2]
                #print("end > start in try 2")
                #print("CELL: [E,S] : ["+str(end+9)+"]["+str(start + 2)+ "]")
            
            newMilage = float(distance)                 # Convert the distance to a float to add to truck
        except:
            if firstColumn[end][start] != '':           # If distance is found, set this as the distance
                distance = firstColumn[start][end+2]
                #print("except1")
            else:                                       # If no distance found, reversing the matrix gives distance
                distance = firstColumn[end][start + 2]
                #print("except2")
            
            newMilage = float(distance) 
        
        # Now we add the distance collected from this package route to a temporary database
        nearestNeighbor.append(newMilage)
        nearestPackage.append(truck.packages[i])
        i += 1

        #truck.milage += newMilage                  # Truck's new milage is calculated

        #print("new milage added: "+ str(newMilage))
        #print("total milage    :  " + str(truck.milage))
    #print(nearestPackage)
    if len(truck.packages) > 0:
        min_value = min(nearestNeighbor)
        smallest_index = nearestNeighbor.index(min_value)
        truck.nextLocation = truck.packages[smallest_index].address

        print(truck.currentLocation + " ---> " + truck.nextLocation)
        print(nearestNeighbor)

        truck.milage += min_value
        print(min_value)
        truck.currentLocation = truck.packages[smallest_index].address
        truck.packages.pop(smallest_index)
        isFirstDropOff += 1
        truckRun(truck, isFirstDropOff)
    else:
        print("complete")
        print("total miles: " + str(truck.milage))

import csv



#We start by placing a truck object into the function argument.
def truckRun(truck):

    firstColumn = []
    with open("WGUPS Distance Table.csv") as distanceCsv:
        distanceData = csv.reader(distanceCsv, delimiter=',')
        for distance in distanceData:
            firstColumn.append(distance)

    print("number of packages in truck: " + str(len(truck.packages)))
    i = 0
    while i < len(truck.packages):
        print("=== Package " + str(i) + " Summary ==================")
            #This compares the inside of each array with a given address
        countRow = 0
        start = 0 #We set the start at 0 because 0 is where the HUB is. The program won't find HUB in the for loop
                #but will still calculate it correctly.
        end = 2   #We need to make this 2 to skip the first column in the csv file.
        if i != 0:
            truck.currentLocation = truck.packages[i - 1].address
        else:
            truck.currentLocation = 'HUB'
        truck.nextLocation = truck.packages[i].address
        print("Current Location: " + truck.currentLocation)
        print("Next    Location: " + truck.nextLocation)

        for address in firstColumn: # The entire row ['name + address', 'address', distance, distance, ...]
                                    # address[1] is the delivery address that should be checked
            if truck.currentLocation == address[1][1: -8]: #If the current trucks address is equal to this other address
                start = countRow
                #print("start found " + str(countRow))
            if truck.nextLocation == address[1][1: -8]:
                end = countRow
                #print("end found " + str(countRow))
            countRow = countRow + 1

        try:
            if firstColumn[start][end] != '':           # If distance is found, set this as the distance
                if start >= end:
                    distance = firstColumn[start][end + 2]
                    print("start > end in try 1")
                    print("CELL: [S,E] : ["+str(start+9)+"]["+str(end + 2)+ "]")
                else:
                    distance = firstColumn[end][start + 2]
                    print("end > start in try 1")
                    print("CELL: [E,S] : ["+str(end+9)+"]["+str(start + 2)+ "]")
            else:                                       # If no distance found, reversing the matrix gives distance
                distance = firstColumn[end][start + 2]
                print("end > start in try 2")
                print("CELL: [E,S] : ["+str(end+9)+"]["+str(start + 2)+ "]")
            
            newMilage = float(distance)                 # Convert the distance to a float to add to truck
        except:
            if firstColumn[end][start] != '':           # If distance is found, set this as the distance
                distance = firstColumn[start][end+2]
                print("except1")
            else:                                       # If no distance found, reversing the matrix gives distance
                distance = firstColumn[end][start + 2]
                print("except2")
            
            newMilage = float(distance) 
        
        truck.milage += newMilage                  # Truck's new milage is calculated

        print("new milage added: "+ str(newMilage))
        i += 1
        print("total milage    :  " + str(truck.milage))
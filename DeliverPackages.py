import csv
from Time import intConvertToTime



# truckRun() is a recursive function that delivers all the packages inside a Truck object's load.
def truckRun(truck, isFirstDropOff, database, time, reportCheck, reportTime, isCheckingReportTime, isThisFinalTruck):
                                                        # We start by placing a Truck object into the function argument.
                                                        # isFirstDropOff lets the program know that the truck should
                                                        #   should start at the Hub and begin delivering from there.
                                                        # database will allow the Truck to mark the packages inside
                                                        #   the database as either 'en route' or 'delivered'.
                                                        # time will help with printing reports on package
                                                        #   delivery status.
    

    # Any Trucks that come after the final Truck will not be checked. If we mark it with 'n' on the
    # isCheckingReportTime this will be skipped.
    if isCheckingReportTime == 'n':
        return



    # This if statement will stop to see if this is happening for the first time. Since this
    #   function is called recursively, we only need to mark the packages 'en route' once.
    #   Without the if statement, delivered packages would be marked as 'en route' causing a bug.
    if isFirstDropOff == 0:
        for packages in truck.packages:
            packages.deliveryStatus = 'en route'



    nearestNeighbor = []                                # This creates a temp list of current distances available to Truck
    
    nearestPackage = []                                 # This creates a temp list of packages still on Truck
    
########## THIS THE THE REPORTS FUNCTIONALITY ###########################################################
    # We check to see at what time (reportTime) the user wants to check the status of all packages
    # in the database. This means all packages, not just the ones in this program.
    if time >= reportTime:      # If it is 8:01 and we want a report by 8:00 we will continue,
        if reportCheck == 0:    # If this is the first time giving a report continue,
            if isThisFinalTruck == 'y': # This report is meant for the final Truck driving not the first Trucks.
                k = 1
                reportCheck = 1         # This ensures only 1 report is given
                while k <= 40:          # Will print out the status of all packages, this is the report
                    print(database.search(k)) 
                    k += 1
    
    # We ask the user in GUI if they are seeking a certain report at a certain time. If they awnser, yes or 'y'
    # we will deliver all the packages up until that time only, as to not have inaccurate reports
    if isCheckingReportTime == 'y':
        if (time > reportTime):
            return
    
##########################################################################################################

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
        # This compares the inside of each array with a given address
        countRow = 0
        start = 0 # We set the start at 0 because 0 is where the HUB is. The program won't find HUB in the for loop
                  #    but will still calculate it correctly.
        end = 2   # We need to make this 2 to skip the first column in the csv file.


        # This will get the address of the current package being compared.
        truck.nextLocation = truck.packages[i].address

        for address in firstColumn: # The entire row ['name + address', 'address', distance, distance, ...]
                                    # address[1] is the delivery address that should be checked
            if truck.currentLocation == address[1][1: -8]: # If the current trucks address is equal to this other address
                start = countRow
            if truck.nextLocation == address[1][1: -8]:
                end = countRow
            countRow = countRow + 1


        # This determines the miles between all package locations and the current location
        # It will add all these distances to a list
        try:
            if firstColumn[start][end] != '':           # If distance is found, set this as the distance
                if start >= end:
                    distance = firstColumn[start][end + 2]
                    #print("start > end in try 1") DEBUGGING TOOL-----------------
                    #print("CELL: [S,E] : ["+str(start+9)+"]["+str(end + 2)+ "]") DEBUGGING TOOL------------
                else:                                   # If firstColumn[start][end] is null, reverseing the matrix gives distance
                    distance = firstColumn[end][start + 2]
                    #print("end > start in try 1") DEBUGGING TOOL------------------
                    #print("CELL: [E,S] : ["+str(end+9)+"]["+str(start + 2)+ "]") DEBUGGING TOOL-----------
            else:                                       # If no distance found, reversing the matrix gives distance
                distance = firstColumn[end][start + 2]
                #print("end > start in try 2") DEBUGGING TOOL------------------
                #print("CELL: [E,S] : ["+str(end+9)+"]["+str(start + 2)+ "]") DEBUGGING TOOL
            
            newMilage = float(distance)                 # Convert the distance to a float to add to nearestNeighbor[]
        except:
            if firstColumn[end][start] != '':           # If distance is found, set this as the distance
                distance = firstColumn[start][end+2]
                #print("except1") DEBUGGING TOOL----------------------------
            else:                                       # If firstColumn[start][end] is null, reverseing the matrix gives distance
                distance = firstColumn[end][start + 2]
                #print("except2") DEBUGGING TOOL----------------------------
            
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

        # If the current package would be delviered after the desired time of the report, we don't
        #   include it on the report.
        if isCheckingReportTime == 'y':
            if (time > reportTime):
                if reportCheck == 0:    # If this is the first time giving a report continue,

                    if isThisFinalTruck == 'y': # This report is meant for the final Truck driving not the first Trucks.
                        k = 1
                        reportCheck = 1         # This ensures only 1 report is given
                        while k <= 40:          # Will print out the status of all packages, this is the report
                            print(database.search(k))
                            k += 1
                return



        # We add the milage driven to the total number of miles drivien by this Truck so far.
        truck.milage += min_value

        # We set the current location to the address of the package we finished dropping off.
        truck.currentLocation = truck.packages[smallest_index].address
        
        
        curr = truck.packages[smallest_index]           # curr represents the current package being dropped off.
        curr.deliveryStatus = 'delivered at ' + str(intConvertToTime(time))# The status is changed to delivered.
        
    
        database.insert(curr.id, curr)                  # The new status is now inserted back into the database.
        
        
        #print(curr.deliveryStatus + " Package ID: " + str(curr.id)) # This will print the package's time delivered 

        truck.packages.pop(smallest_index)              # Removes the package from the Trucks load.

        truckRun(truck, 1, database, time, reportCheck, reportTime, isCheckingReportTime, isThisFinalTruck) 
                                                        # A recursive function that will keep calling itself
                                                        #   until all packages are delivered.
                                                        #   Note that we now enter a 1 instead of a 0
                                                        #   for the second argument. This is to tell
                                                        #   The function that this isn't the initial run
                                                        #   but a recursive call.
    
    # If no more packages remain on the Truck, we return the total milage driven by this Truck.
    else:
        #print("total miles: " + str(truck.milage))     # This prints the total milage for this Truck.



        # Incase all packages are delivered before the reportTime is reached 
        # (finished at 10am but checking till 11am), we will finish the program 
        # after the isThisFinalTruck is complete, and give the report then.

        if reportCheck == 0:    # If this is the first time giving a report continue,

            if isThisFinalTruck == 'y': # This report is meant for the final Truck driving not the first Trucks.
                k = 1
                reportCheck = 1         # This ensures only 1 report is given
                while k <= 40:          # Will print out the status of all packages, this is the report
                    print(database.search(k))
                    k += 1
        
                

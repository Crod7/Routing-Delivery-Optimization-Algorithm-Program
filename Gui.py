from DeliverPackages import truckRun
from Time import intConvertToTime

# This function is called at the start of the program and managers user input. It returns data depending
# on user needs. THIS PART OF THE PROGRAM IS TO BE REPLACED WITH A BETTER GUI IN THE FUTURE.
def mainMenu(truck1, truck2, truck3, database):
    print("-----UPS Routing Program-----")
    print("1. Get total milage")
    print("2. Check status of all packages at 9:00am")
    print("3. Check status of all packages at 10:00am")
    print("4. Check status of all packages at 1:00pm")
    print("5. Check status of all packages at a time of your choosing")
    print("6. Check status of a single package at the time of your choosing")
    print("7. Exit")
    print("-----------------------------")


    try:
        select = int(input("Please make a selection, enter a number: "))
    except:
        print("\nEnter a Number!\n")
        select = 0

    if select == 1:
        reportTime = 24     # This is the time the report will be returned at.
        #   name(TruckObject, starting milage, database, startingTime, reportCheck, reportTime, isCheckingReportTime, isThisFinalTruck)
        truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'n'         , 'n')       
        truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'y'                 , 'n'         , 'n')       
        truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'y'                 , 'n'         , 'n')
        print("\nTotal Milage of All 3 Trucks together: " + str(round(truck1.milage + truck2.milage + truck3.milage, 2)) +"\n")       

    elif select == 2:
        print("\n\n===================== PACKAGES STATUS at 9:00AM =========================")
        print("=========================================================================")  
        reportTime = 9     # This is the time the report will be returned at.
        #   name(TruckObject, starting milage, database, startingTime, reportCheck, reportTime, isCheckingReportTime, isThisFinalTruck)
        truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'y'         , 'n')       
        truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'n'                 , 'n'         , 'n')       
        truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'n'                 , 'n'         , 'n')
        print("\nTotal Milage of All 3 Trucks together at this time: " + str(round(truck1.milage + truck2.milage + truck3.milage, 2)) +"\n")       
        print("=========================================================================")     
        print("=========================================================================\n")

    elif select == 3:
        print("\n\n===================== PACKAGES STATUS at 10:00AM =========================")
        print("=========================================================================")  
        reportTime = 10     # This is the time the report will be returned at.
        #   name(TruckObject, starting milage, database, startingTime, reportCheck, reportTime, isCheckingReportTime, isThisFinalTruck)
        truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'n'         , 'n')       
        truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'y'                 , 'y'         , 'n')       
        truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'n'                 , 'n'         , 'n')
        print("\nTotal Milage of All 3 Trucks together at this time: " + str(round(truck1.milage + truck2.milage + truck3.milage, 2)) +"\n")       
        print("=========================================================================")     
        print("=========================================================================\n")

    elif select == 4:
        print("\n\n===================== PACKAGES STATUS at 1:00PM =========================")
        print("=========================================================================")  
        reportTime = 13     # This is the time the report will be returned at.
        #   name(TruckObject, starting milage, database, startingTime, reportCheck, reportTime, isCheckingReportTime, isThisFinalTruck)
        truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'n'         , 'n')       
        truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'y'                 , 'n'         , 'n')       
        truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'y'                 , 'y'         , 'n')
        print("\nTotal Milage of All 3 Trucks together at this time: " + str(round(truck1.milage + truck2.milage + truck3.milage, 2)) +"\n")       
        print("=========================================================================")     
        print("=========================================================================\n")

    elif select == 5:
        reportTime = float(input("Please enter a time (ex: 9.1 -> 9:06am, 13.5 -> 1:30pm) "))
        
        print("\n\n===================== PACKAGES STATUS at " + str(intConvertToTime(reportTime)) + " =========================")
        print("=========================================================================")  
        #   name(TruckObject, starting milage, database, startingTime, reportCheck, reportTime, isCheckingReportTime, isThisFinalTruck)
        if (reportTime >= 8 and reportTime < 9.0835):
            truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'y'         , 'n')
            truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'n'                 , 'n'         , 'n')       
            truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'n'                 , 'n'         , 'n')            
        elif (reportTime >= 9.0835 and reportTime < 10.3335):
            truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'n'         , 'n')
            truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'y'                 , 'y'         , 'n')       
            truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'n'                 , 'n'         , 'n')        
        elif (reportTime >= 10.3335):
            truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'n'         , 'n')
            truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'y'                 , 'n'         , 'n')       
            truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'y'                 , 'y'         , 'n')  
        else:
            print("\n============= No trucks have left yet =============\n")
        print("\nTotal Milage of All 3 Trucks together at this time: " + str(round(truck1.milage + truck2.milage + truck3.milage, 2)) +"\n")       
        print("=========================================================================")     
        print("=========================================================================\n")

    elif select == 6:
        reportTime = float(input("Please enter a time (ex: 9.1 -> 9:06am, 13.5 -> 1:30pm):\n "))
        packageId = int(input("Enter a number 1-40 to look up the package detail at this moment in time:\n"))
        
        print("\n\n===================== PACKAGES STATUS at " + str(intConvertToTime(reportTime)) + " =========================")
        print("=========================================================================")  
        #   name(TruckObject, starting milage, database, startingTime, reportCheck, reportTime, isCheckingReportTime, isThisFinalTruck)
        if (reportTime >= 8 and reportTime < 9.0835):
            truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'y'         , 'y')
            truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'n'                 , 'n'         , 'y')       
            truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'n'                 , 'n'         , 'y')
            print("\n============= RESULT FOR PACKAGE # " + str(database.search(packageId).id) + " =============\n")
            print("Package ID: " + str(database.search(packageId).id))
            print("Package Address: " + (database.search(packageId).address) +", "+(database.search(packageId).city) +", "+(database.search(packageId).state)+" "+ str(database.search(packageId).zipCode))
            print("Package Weight: " + str(database.search(packageId).weight))
            print("Package Delivery Deadline: " + (database.search(packageId).deadline))
            print("Package Delivery Status: " + (database.search(packageId).deliveryStatus))  
            print("\n======================================================\n")

        elif (reportTime >= 9.0835 and reportTime < 10.3335):
            truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'n'         , 'y')
            truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'y'                 , 'y'         , 'y')       
            truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'n'                 , 'n'         , 'y')
            print("\n============= RESULT FOR PACKAGE # " + str(database.search(packageId).id) + " =============\n")
            print("Package ID: " + str(database.search(packageId).id))
            print("Package Address: " + (database.search(packageId).address) +", "+(database.search(packageId).city) +", "+(database.search(packageId).state)+" "+ str(database.search(packageId).zipCode))
            print("Package Weight: " + str(database.search(packageId).weight))
            print("Package Delivery Deadline: " + (database.search(packageId).deadline))
            print("Package Delivery Status: " + (database.search(packageId).deliveryStatus))  
            print("\n======================================================\n")     
        
        elif (reportTime >= 10.3335):
            truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'n'         , 'y')
            truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'y'                 , 'n'         , 'y')       
            truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'y'                 , 'y'         , 'y')
            print("\n============= RESULT FOR PACKAGE # " + str(database.search(packageId).id) + " =============\n")
            print("Package ID: " + str(database.search(packageId).id))
            print("Package Address: " + (database.search(packageId).address) +", "+(database.search(packageId).city) +", "+(database.search(packageId).state)+" "+ str(database.search(packageId).zipCode))
            print("Package Weight: " + str(database.search(packageId).weight))
            print("Package Delivery Deadline: " + (database.search(packageId).deadline))
            print("Package Delivery Status: " + (database.search(packageId).deliveryStatus))  
            print("\n======================================================\n")
  
        else:
            print("\n============= No trucks have left yet =============\n")
            print("\n============= RESULT FOR PACKAGE # " + str(database.search(packageId).id) + " =============\n")
            print("Package ID: " + str(database.search(packageId).id))
            print("Package Address: " + (database.search(packageId).address) +", "+(database.search(packageId).city) +", "+(database.search(packageId).state)+" "+ str(database.search(packageId).zipCode))
            print("Package Weight: " + str(database.search(packageId).weight))
            print("Package Delivery Deadline: " + (database.search(packageId).deadline))
            print("Package Delivery Status: " + (database.search(packageId).deliveryStatus))  
            print("\n======================================================\n")         

        print("\nTotal Milage of All 3 Trucks together at this time: " + str(round(truck1.milage + truck2.milage + truck3.milage, 2)) +"\n")       
        print("=========================================================================")     
        print("=========================================================================\n")

    elif select == 7:
        exit()
        return

    else:
        print("\nThat is not an option.\n")
        mainMenu(truck1, truck2, truck3, database)
    return

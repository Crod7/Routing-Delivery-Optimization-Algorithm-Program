from DeliverPackages import truckRun

# This function is called at the start of the program and managers user input. It returns data depending
# on user needs.
def mainMenu(truck1, truck2, truck3, database):
    print("-----UPS Routing Program-----")
    print("1. Get total milage")
    print("2. Check status of packages at 9:00am")
    print("3. Check status of packages at 10:00am")
    print("4. Check status of packages at 1:00pm")
    print("5. Exit")
    print("-----------------------------")



    try:
        select = int(input("Please make a selection, enter a number: "))
    except:
        print("\nEnter a Number!\n")
        select = 0

    if select == 1:
        reportTime = 24     # This is the time the report will be returned at.
        #   name(TruckObject, starting milage, database, startingTime, reportCheck, reportTime, isCheckingReportTime, isThisFinalTruck)
        truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'n')       
        truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'y'                 , 'n')       
        truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'y'                 , 'n')
        print("\nTotal Milage of All 3 Trucks together: " + str(round(truck1.milage + truck2.milage + truck3.milage, 2)) +"\n")       

    elif select == 2:
        print("\n\n===================== PACKAGES STATUS at 9:00AM =========================")
        print("=========================================================================")  
        reportTime = 9     # This is the time the report will be returned at.
        #   name(TruckObject, starting milage, database, startingTime, reportCheck, reportTime, isCheckingReportTime, isThisFinalTruck)
        truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'y')       
        truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'n'                 , 'n')       
        truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'n'                 , 'n')
        print("\nTotal Milage of All 3 Trucks together: " + str(round(truck1.milage + truck2.milage + truck3.milage, 2)) +"\n")       
        print("=========================================================================")     
        print("=========================================================================\n")

    elif select == 3:
        print("\n\n===================== PACKAGES STATUS at 10:00AM =========================")
        print("=========================================================================")  
        reportTime = 10     # This is the time the report will be returned at.
        #   name(TruckObject, starting milage, database, startingTime, reportCheck, reportTime, isCheckingReportTime, isThisFinalTruck)
        truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'n')       
        truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'y'                 , 'y')       
        truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'n'                 , 'n')
        print("\nTotal Milage of All 3 Trucks together: " + str(round(truck1.milage + truck2.milage + truck3.milage, 2)) +"\n")       
        print("=========================================================================")     
        print("=========================================================================\n")

    elif select == 4:
        print("\n\n===================== PACKAGES STATUS at 1:00PM =========================")
        print("=========================================================================")  
        reportTime = 13     # This is the time the report will be returned at.
        #   name(TruckObject, starting milage, database, startingTime, reportCheck, reportTime, isCheckingReportTime, isThisFinalTruck)
        truckRun(truck1     , 0              , database, 8           , 0          , reportTime, 'y'                 , 'n')       
        truckRun(truck2     , 0              , database, 9.0835      , 0          , reportTime, 'y'                 , 'n')       
        truckRun(truck3     , 0              , database, 10.3335     , 0          , reportTime, 'y'                 , 'y')
        print("\nTotal Milage of All 3 Trucks together: " + str(round(truck1.milage + truck2.milage + truck3.milage, 2)) +"\n")       
        print("=========================================================================")     
        print("=========================================================================\n")

    elif select == 5:
        exit()
        return

    else:
        print("\nThat is not an option.\n")
        mainMenu(truck1, truck2, truck3, database)
    return

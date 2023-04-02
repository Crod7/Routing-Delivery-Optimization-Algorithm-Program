# Name: Carlos Rodriguez
# Student ID: 010515761

from Run import run

# This starts up the program. Run the program on main.

i = 1   # i is used for the while loop.
# The while loops only purpose is to help create new instances of run(). The program terminates inside of run().
while i == 1:



    # The bulk of the program is run on 'Run.py'. The reason for this is to create an instance
    # of the program, the user can check the data in the Hash Table at multiple different points
    # without causing issues. Each time a new check is done, a new instance is created.
    run() 


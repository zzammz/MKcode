

import inspect
import sys

# ========================= common
def log_trace(func_name):
    print ("\n----- " + func_name + "() -----")
    #print (inspect.stack()[1][3])
    #frame = inspect.currentframe()
    #print (inspect.getframeinfo(frame).function)
    #print(inspect.getframeinfo(inspect.currentframe()).function)
    return



def examples_conditions():
    log_trace("examples_conditions")

    print ("")
    print ("-- if")
    a = 3   # A is a positive number
    if a > 0:
        print('A is a positive number')

    a = 3
    if a < 0:
        print('A is a negative number')
    else:
        print('A is a positive number')

    a = 0
    if a > 0:
        print('A is a positive number')
    elif a < 0:
        print('A is a negative number')
    else:
        print('A is zero')

    a = 3
    if a > 0:
        print('A is positive')
    else:
        print('A is negative')  # first condition met, 'A is positive' will be printed

    a = 0
    if a > 0:
        if a % 2 == 0:
            print('A is a positive and even integer')
        else:
            print('A is a positive number')
    elif a == 0:
        print('A is zero')
    else:
        print('A is a negative number')

    return

def condition_and_local_operators():
    log_trace("condition_and_local_operators")

    print("")
    print("-- condition & logical ops")
    a = 0
    if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
    elif a > 0 and a % 2 != 0:
        print('A is a positive integer')
    elif a == 0:
        print('A is zero')
    else:
        print('A is negative')

    user = 'James'
    access_level = 3
    if user == 'admin' or access_level >= 4:
        print('Access granted!')
    else:
        print('Access denied!')

    return



# ========================= main
examples_conditions()
condition_and_local_operators()



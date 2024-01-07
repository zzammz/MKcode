

import inspect
import sys

# ========================= common
def log_trace(func_name):
    print ("\n--- " + func_name + "()")
    #print (inspect.stack()[1][3])
    #frame = inspect.currentframe()
    #print (inspect.getframeinfo(frame).function)
    #print(inspect.getframeinfo(inspect.currentframe()).function)
    return


# ========================= algorithms

# ----------------- push zeroes to end
def PushZeroesToEnd(p_array):
    Plog_trace("PushZeroesToEnd")
    print ("input array: " + str(p_array))
    len_array = len(p_array)
    for ictr in range (0, len_array, 1):
        if(p_array[ictr] == 0):
            for jctr in range (ictr, len_array-1, 1):
                p_array[jctr] = p_array[jctr+1]
            p_array[jctr+1] = 0
    print("output array: " + str(p_array))
    return

def TEST_PushZeroestoEnd():
    test_array = [1, 2, 0, 4, 3, 0, 5, 0]
    #test_array = [1, 0, 3, 5, 0]
    PushZeroesToEnd(test_array)
    return




# ========================= main

TEST_PushZeroestoEnd()







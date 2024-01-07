

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

# --------------- find dupes

def FindDupes (p_array):
    log_trace("FindDupes")
    dupe_response = -1
    ictr = 0
    jctr = 0
    len_array = len(p_array)
    for ictr in range (0, len_array-1):
        for jctr in range (ictr+1, len_array):
            if p_array[ictr] == p_array[jctr]:
                dupe_response = p_array[ictr]
                return dupe_response

    return dupe_response


def FindDupes2 (p_array):
    log_trace("FindDupes2")
    p_array.sort()
    len_array = len(p_array)
    if len_array <= 1:
        return -1
    ictr = 0
    for ictr in range (0, len_array-1, 1):
        if p_array[ictr] == p_array[ictr+1]:
            return p_array[ictr]
    return -1


def TEST_FindDupes():
    test_array = [11, 13, 7, 11, 1, 3, 8, 4]
    response_dupe_check = FindDupes(test_array)
    if response_dupe_check == -1:
        print("No duplicates were found")
    else:
        print("Duplicate number: " + str(response_dupe_check))

    response_dupe_check = FindDupes2(test_array)
    if response_dupe_check == -1:
        print("No duplicates were found")
    else:
        print("Duplicate number: " + str(response_dupe_check))

    return





# ========================= main

TEST_FindDupes()







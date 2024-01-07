

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
    PrintMe("FindDupes")
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
    PrintMe("FindDupes2")
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



# ----------------- movies on flight
def MoviesOnFlight(p_array, p_duration, p_max_gap):
    PrintMe("MoviesOnFlight")
    p_array.sort(reverse=True)
    for ictr in range (0, len(p_array)-1, 1):
        time_spent = p_duration - p_array[ictr] - p_array[ictr+1]
        if time_spent > 0 and time_spent <= p_max_gap:
            print(p_duration - p_array[ictr] - p_array[ictr+1])
            print ("[" + str(p_array[ictr]) + ", " + str(p_array[ictr+1]) + "]")
            return

    print ("Could not find 2 movies to watch within the " + str(p_duration) + " time period")
    return


def TEST_MoviesOnFlight():
    movie_array = [90, 85, 75, 60, 120, 150, 125]
    flight_duration = 250
    max_gap_allowed = 30
    MoviesOnFlight(movie_array, flight_duration, max_gap_allowed)
    return

# ----------------- push zeroes to end
def PushZeroesToEnd(p_array):
    PrintMe("PushZeroesToEnd")
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


TEST_FindDupes()
TEST_MoviesOnFlight()
TEST_PushZeroestoEnd()







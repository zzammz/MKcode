

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


# ----------------- movies on flight
def MoviesOnFlight(p_array, p_duration, p_max_gap):
    log_trace("MoviesOnFlight")
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


# ========================= main

TEST_MoviesOnFlight()








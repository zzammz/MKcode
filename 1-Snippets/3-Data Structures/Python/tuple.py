
# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

#https://www.w3schools.com/python/python_ref_string.asp
#https://www.afternerd.com/blog/python-enumerate/
# https://www.w3schools.com/css/default.asp
#https://www.geeksforgeeks.org/python-strings/
#https://www.geeksforgeeks.org/regular-expressions-python-set-1-search-match-find/
#https://rafal.io/archives.html
#https://regexr.com/


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


# =========== 


def examples_tuple():
    log_trace("examples_tuples")
    my_coord = (2, 3)
    print(my_coord)
    print(my_coord[0])

    print("")
    my_coords = [ (101, 102), (204, 205), (306, 307) ]
    print(my_coords)
    print(my_coord[1])
    print (my_coords[2][0])

    return


# ========================= main

examples_tuple()







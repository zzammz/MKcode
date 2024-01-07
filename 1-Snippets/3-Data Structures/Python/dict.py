
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




def examples_dict():
    log_trace("examples_dict")
    my_dict = {
        "Jan" : "January",
        "Feb" : "February",
        "Mar" : "March",
        "Apr" : "April",
        "May" : "May",
        "Jun" : "June",
        "Jul" : "July",
        "Aug" : "August",
        "Sep" : "September",
        "Oct" : "October",
        "Nov" : "November",
        "Dec" : "December",
    }
    # access dict
    print (my_dict)
    print (my_dict.get("Oct"))
    print(my_dict.get("Oct2", "not a valid key"))
    print ("")

    #loop through dict
    for xval in my_dict.keys():
        print(xval)
    for yval in my_dict.items():
        print(yval[0] + " " + yval[1])
    for (xval, yval) in my_dict.items():
        print(xval + " --- " + yval)
    print("")

    #update dict
    print(my_dict["Feb"])
    my_dict["Jul"] = "Julius"
    print(my_dict)
    return



# ========================= main

examples_dict()







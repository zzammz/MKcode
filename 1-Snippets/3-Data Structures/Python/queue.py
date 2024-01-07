
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


# ========================= data structures

def DS_queue():
    log_trace("DS_queue")
    fruits = []
    fruits.append("apple")
    fruits.append("banana")
    fruits.append("mango")
    print (fruits)
    print("popped: " + fruits.pop(0))
    print(fruits)
    fruits.append("cherry")
    print(fruits)
    print("popped: " + fruits.pop(0))
    print(fruits)
    return



# ========================= main
DS_queue()







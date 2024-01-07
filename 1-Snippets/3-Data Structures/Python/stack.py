
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
    return


# ========================= data structures




def DS_stack():
    log_trace("DS_stack")
    fruits = []
    fruits.append("apple")
    fruits.append("banana")
    fruits.append("mango")
    print (fruits)
    print("popped: " + fruits.pop(-1))
    print(fruits)
    fruits.append("cherry")
    print(fruits)
    print("popped: " + fruits.pop(-1))
    print(fruits)
    return


# ========================= main
DS_stack()






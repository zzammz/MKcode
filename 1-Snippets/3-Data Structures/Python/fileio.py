
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



import os
# =========== file i/o
def examples_fileio():
    log_trace("examples_fileio")

    print("- write")
    file_emp = open("employees.txt", "w")
    file_emp.write("Dwight - Sales\n")
    file_emp.write("Michael - Manager\n")
    file_emp.close()

    print("")
    print("- append")
    file_emp = open("employees.txt", "a")
    file_emp.write("Kelly - Customer service\n")
    file_emp.close()

    print("")
    print("- read")
    file_emp = open ("employees.txt", "r")
    for emp in file_emp.readlines():
        print (emp)
    file_emp.close()

    print("")
    print("- path")
    is_my_path = os.path.exists ("/Users/muzzammilkhan/Desktop/MKhome/Dev/Python/three")
    print (is_my_path)

    return



# ========================= main

TESTGRP_fileio()




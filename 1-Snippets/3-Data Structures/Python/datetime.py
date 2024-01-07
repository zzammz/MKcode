
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


# ---- datetime
import datetime
def examples_datetime():
    dt_obj = datetime.datetime.now()
    print (dt_obj)
    print (dt_obj.month)
    return


def check_time_spent():
    dt_start = datetime.datetime.now()
    tmp_array = []
    sum_array = 0
    max_ctr = 10000
    for ictr in range(0, max_ctr):
        tmp_array.append(ictr)
    for ictr in range(0, max_ctr):
        sum_array = sum(tmp_array[0:ictr])

    dt_end = datetime.datetime.now()
    dt_diff = dt_end - dt_start
    print ("{}.{} secs".format(str(dt_diff.seconds), str(dt_diff.microseconds)))
    return


def check_time_spent2():
    tmp_array = []
    sum_array = 0
    max_ctr = 10000000
    for ictr in range(0, max_ctr):
        tmp_array.append(ictr)

    #--- forloop
    dt_start = datetime.datetime.now()
    for ictr in range(0, max_ctr):
        jj = tmp_array[ictr]

    dt_end = datetime.datetime.now()
    dt_diff = dt_end - dt_start
    print ("forloop: {}.{} secs".format(str(dt_diff.seconds), str(dt_diff.microseconds)))

    #--- enumerate
    dt_start = datetime.datetime.now()
    for idx, val in enumerate(tmp_array):
        jj = val

    dt_end = datetime.datetime.now()
    dt_diff = dt_end - dt_start
    print ("enum: {}.{} secs".format(str(dt_diff.seconds), str(dt_diff.microseconds)))

    return






# ========================= main

examples_datetime()










import inspect
import sys

# ========================= common
def log_trace(func_name):
    print ("\n----- " + func_name + "() -----")
    #print (inspect.stack()[1][3])
    #frame = inspect.currentframe()
    #print (inspect.getframeinfo(frame).function)
    #print(inspect.getframeinfo(inspect.currentframe()).function)
    return


def list_conversions():
    log_trace("list_conversions")
    print("")
    print("-- string to list")

    language = 'Python'
    a, b, c, d, e, f = language
    print(a)  # P
    print(b)  # y
    print(c)  # t
    print(d)  # h
    print(e)  # o
    print(f)  # n

    print("")
    print("-- list to set")
    list2 = ["101", "102", "103", "101"]
    print ("list: " + str(list2))

    set2 = set(list2) # will drop the duplicate '101'
    print ("set: " + str(set2) )

    return


def tuple_conversions():
    log_trace("tuple_conversions")

    print("")
    print("-- tuple to list")

    tpl = ('item1', 'item2', 'item3', 'item4')
    lst = list(tpl)
    print ("tuple: " + str(tpl) )

    print("")
    fruits_tpl = ('banana', 'orange', 'mango', 'lemon')
    print("tuple: " + str(fruits_tpl) )
    fruits_list = list(fruits_tpl)
    print("list: " + str(fruits_list) )
    fruits_list[0] = 'apple'
    print("list: "+ str(fruits_list))  # ['apple', 'orange', 'mango', 'lemon']

    print("")
    print("-- list to tuple")

    fruits_tpl2 = tuple(fruits_list)
    print("tuple: " + str(fruits_tpl2))  # ('apple', 'orange', 'mango', 'lemon')

    return




# ========================= main
list_conversions()
tuple_conversions()



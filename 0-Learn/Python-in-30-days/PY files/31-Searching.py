

import inspect
import sys

# ========================= common
def log_trace(func_name):
    print ("\n----- " + func_name + "() -----")
    #print (inspect.stack()[1][3])
    #frame = inspect.currentframe()
    #print (inspect.getframeinfo(frame).function)
    #print(inspect.getframeinfo(inspect.currentframe()).function) #
    return


def find_in_list(mylist, find_value):
    find_pos = -1
    if find_value in mylist:
        find_pos = mylist.index(find_value)
    return find_pos



def SearchStrings():
    log_trace("SearchStrings")

    #print ("")
    #print ("-- basics")

    fullstr = "hello darkness my old friend"

    find_str = "e"
    print ("searching for '" + find_str + "' : " + str(fullstr.find(find_str)))

    find_str = "x"
    print("searching for '" + find_str + "' : " + str(fullstr.find(find_str)))

    find_str = ""
    print("searching for '" + find_str + "' : " + str(fullstr.find(find_str)))

    return



def SearchLists():
    log_trace("SearchLists")

    print("")
    print("-- find index")

    fruits = ['banana', 'orange', 'mango', 'lemon']
    print(fruits)

    find_value = "mango"
    print ("searchig for '" + find_value + "': "+ str(find_in_list(fruits, find_value)))

    find_value = "cherry"
    print("searchig for '" + find_value + "': " + str(find_in_list(fruits, find_value)))

    find_value = ""
    print("searchig for '" + find_value + "': " + str(find_in_list(fruits, find_value)))

    return



# ========================= main
SearchStrings()
SearchLists()



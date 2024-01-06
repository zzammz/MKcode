
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

# ========================= basics

#----------------- strings
def examples_string():

    log_trace ("examples_string")
    str_firstname = "john"
    str_lastname = "doe"
    iAge = 40
    str_fullname = str_firstname + " " + str_lastname
    print(str_fullname)

    str_myname = "my name is {0} {1}".format(str_firstname, str_lastname)
    print (str_myname)
    print ("{0} - {1}".format("jane", "boyd"))

    print ("His fullcap name is: " + str_fullname.upper() + " age: " + str(iAge))
    print ("His capitalized name is: " + str_fullname.capitalize() + " age: " + str(iAge))
    print ("and name length is: " + str(len(str_fullname)))
    print ("")
    print ("first char is: " + str_fullname[1])
    print ("index of 'o' at: " + str(str_fullname.index("o")) )
    print ("replacing j with GG: " + str_fullname.replace("j", "GG"))
    print("replacing o with XX: " + str_fullname.replace("o", "XX"))

    print("")
    str_find = "o"
    if (str_fullname.find(str_find) >= 0):
        print ("found the value: " + str_find)
    else:
        print ("cannot found: " + str_find)
    return

def examples_number():
    log_trace("examples_numbers")
    num1 = 42
    print("num1 = " + str(num1))
    num2 = 32.78
    print("actual num2 = " + str(num2))
    print("round(num2) = " + str(round(num2)))
    print("(round(num2,1) = " + str(round(num2, 1)))
    print("round(num2,2) = " + str(round(num2, 2)))
    return


def examples_input():
    log_trace("examples_input")
    num1 = input ("enter num1: ")
    num2 = input ("enter num2: ")
    result = float(num1) + float(num2)
    print ("result= " + str(result))
    return

def examples_list():
    log_trace("examples_list")
    friends_list = ["david", "mike", "jim", "dwight", "oscar"]
    print(friends_list)
    print(friends_list[1:3])
    print (friends_list[-1])
    friends_list[1] = "stanley"
    print(friends_list)
    print("")

    # assigning list to another does not create a duplicate
    full_list = friends_list
    #friends_list2 = friends_list.copy()
    #print(full_list)
    friends_list[1] = "creed"
    print(full_list)
    print(friends_list)
    #print (friends_list2)

    print("")

    # list functions
    lucky_nums = [1, 3, 5, 7]
    friends_list.extend(lucky_nums)
    print("extended: ")
    print(friends_list)

    friends_list.insert(1, "mike")
    print("insert at 1:")
    print(friends_list)

    friends_list.remove("creed")
    print("remove creed:")
    print(friends_list)

    print("count of items: " + str(len(friends_list)))
    friends_list.pop()
    print("count of items: " + str(len(friends_list)))

    print("")
    print("sort & reverse")
    friends_list.sort()
    print(friends_list)
    friends_list.reverse()
    print(friends_list)
    return



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

def examples_set():
    log_trace("examples_set")
    show_fruits_examples = True
    if show_fruits_examples:
        my_fruits = {"apple", "mango", "banana", "cherry"}
        print (my_fruits)
        if "apple" in my_fruits:
            print("apple in included in my_fruits")

    # create set from values


    # create set from list / array


    # remove list duplicates via set
    mylist3 = [3, 5, 7, 1, 11, 9, 3]
    print (mylist3)
    myset3 = set (mylist3)
    print(myset3)


    # check set intersection

    # check for subset

    # set to list / array

    return

# ---- funcs

def examples_func(name1, name2):
    print("hello to {0} and {1}".format(name1, name2))
    return

def examples_func2(num):
    return num * num * num


# ========================= main
# ------ main
#print ("Hello, World!\n")
#examples_string()
#examples_number()
#examples_input()
#examples_list()
#examples_tuple()
#examples_dict()
examples_set()

#examples_func("jack", "pirate")
#print("cube is: {0}".format(str(examples_func2(3))))


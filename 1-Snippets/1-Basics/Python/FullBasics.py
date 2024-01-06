
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

    print("")
    print("- other methods")
    test_str = "hello darkness my old friend"
    print (test_str.count("e"))
    print (test_str.endswith(("e")))
    print (test_str.find("e"))
    print (test_str.rfind("e"))
    print (test_str.replace("e", "X"))

    print("- is()")
    str2 = "Hello123"
    print(str2.isalnum())
    print(str2.isalpha())
    #str3 = "234"
    #print (str3.isdecimal())

    #tuples
    print("- tuples")
    myTuple = ("one", "two", "three")
    strTuple = "#".join(myTuple)
    print (strTuple)
    str5 = "I can eat many grapes in a day"
    print (str5.partition("grapes"))


    #list
    print("- list")
    str6 = "I like apples"
    print (str6.replace("apples", "mangoes"))
    str7 = "welcome to the jungle"
    print (str7.split())


    # trim spaces
    print("- trim")
    str4 = "     banana   "
    print ("[" + str4.lstrip() + "]")
    print ("[" + str4.rstrip() + "]")
    print ("[" + str4.lstrip().rstrip() + "]")

    str8 = "57"
    print (str8.zfill(7))


    return

def check_vowel_count(test_str):
    log_trace("check_vowel_count")
    vowel_list = "AEIOUaeiou"
    vowel_count = 0
    vowel_found = []
    for achar in test_str:
        if achar in vowel_list:
            vowel_count += 1
            vowel_found.append(achar)
    print ("vowel count: " + str(vowel_count))
    print (vowel_found)
    return

def check_exact_str():
    log_trace("check_exact_str")
    str101 = "darkness"
    str102 = "darkness"
    if str101 == str102:
        print ("strings are same")
    else:
        print ("strings are not same")
    return

def check_str_content():
    log_trace("check_str_content")
    str101 = "darkness"
    str102 = "nessdark"
    if sorted(str101) == sorted(str102):
        print ("strings have same content")
    else:
        print ("strings do not have same content")
    return


def TESTGRP_string_methods():
    examples_string()
    str2 = "hello darkness my old friend"
    #check_vowel_count(str2)
    #check_exact_str()
    #check_str_content()
    return


#----------------- numbers
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

def examples_if():
    log_trace("examples_if")

    print("- if")
    ismale = True
    if ismale:
        print ("you are a male")
    else:
        print ("you are a lady")

    print("")
    print("- multi if")
    istall = True
    if ismale and istall:
        print("you are both male & tall")
    elif ismale and not(istall):
        print("you are a tall male")
    elif not(ismale) and istall:
        print ("you are a tall lady")
    else:
        print ("you are a short lady")

    num1 = 1
    num2 = 2
    if num1 == num2:
        print ("numbers are equal")
    else:
        print("numbers are equal")

    return

def examples_loop():
    log_trace("examples_loop")

    print("- while")
    ictr = 4
    while ictr >= 4:
        print ("ictr: " + str(ictr))
        ictr -= 1

    print("")
    print("- for; in")
    for aletter2 in "Jacky":
        print ("aletter2: " + aletter2)

    print("")
    print("- for: range")
    for ictr2 in range (3):
        print("ictr2: " + str(ictr2))

    print("")
    print("- for: list")
    friendlist = ["jim", "pam", "karen"]
    for afriend in friendlist:
        print ("friend: " + afriend)

    print("")
    print("- for: list range")
    for ictr3 in range (len(friendlist)):
        print ("friend: " + friendlist[ictr3])

    return

# catch broad errors with just 'except'
# or catch specific errors with specific error codes
def examples_tryexcept():
    log_trace("examples_loop")

    print("- basic try/except")
    #my_int1 = 1
    try:
        print(my_int1)
    except NameError:
        print("error: variable not defined")
    except:
        print ("error: something else went wrong")
    else:
        print ("all success - nothing wrong")
    finally:
        print("executing this whether error or not")

    print("")
    print("- basic try/except 2")
    global_err = ""
    try:
        num2 = int (input ("enter a number: "))
        print(num2)
    except ZeroDivisionError as my_err: #for testing purposes only
        global_err = my_err
        print("error: divided by zero")
    except ValueError as my_err:
        global_err = my_err
        print("error: invalid input")
    except: #for all other errors
        print ("error: broad exception")
    finally:
        print ("we are here whether error or not")

    print ("error msg: [" + global_err + "]")

    return

# ---- funcs
def examples_func(name1, name2):
    print("hello to {0} and {1}".format(name1, name2))
    return

def examples_func2(num):
    return num * num * num


# =========== data strucutres: list, tuples, sets
def examples_list():
    log_trace("examples_list")
    print("- list content manipulation")
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
    print("- list funcs")
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
    print("- sort & reverse")
    print("sort & reverse")
    friends_list.sort()
    print(friends_list)
    friends_list.reverse()
    print(friends_list)

    print("")
    print("- list of lists")
    num_grid = [
        [1, 2, 3],
        [11, 12, 13],
        [101, 102, 103],
        [0]
    ]
    for row in num_grid:
        print "row:"
        print row
        for col in row:
            print col

    print("")
    print("- translate")
    full_phrase = "hello darkness my old friend"
    print "full phase: " + full_phrase
    translated_phrase = ""
    for aletter in full_phrase:
        if aletter in "AaEeIiOoUu":
            translated_phrase = translated_phrase + "."
        else:
            translated_phrase = translated_phrase + aletter
    print translated_phrase

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
    print ("- fruits")
    show_fruits_examples = True
    if show_fruits_examples:
        my_fruits = {"apple", "mango", "banana", "cherry"}
        print (my_fruits)
        if "apple" in my_fruits:
            print("apple in included in my_fruits")

    # create set from values
    print("")
    print("- set from values")
    my_vegs = set ( ("cilantro", "mint", "carrots"))
    print (my_vegs)


    # create set from list / array
    print("")
    print("- set from list")
    my_list2 = ["hello", "hi", "howdy"]
    my_set2 = set (my_list2)
    print(my_list2)
    print(my_set2)


    # remove list duplicates via set
    print("")
    print ("- remove dupes")
    mylist3 = [3, 5, 7, 1, 11, 9, 3]
    print (mylist3)
    myset3 = set (mylist3)
    print(myset3)


    # check set intersection of 2 or more
    print("")
    print("- set intersection")
    my_list101 = ["car", "bike", "helmet"]
    my_list102 = ["bicycle", "helmet", "airpump"]
    my_list103 = ["taekowndo", "dojo", "helmet"]
    my_set101 = set (my_list101)
    my_set102 = set (my_list102)
    my_set103 = set (my_list103)
    common_set2 = my_set101.intersection(my_set102)
    print (common_set2)
    common_set3 = my_set101.intersection(my_set102, my_set103)
    print(common_set3)

    # check for subset
    print("")
    print("- set subset")
    my_issubset = my_set101.issubset(my_set101)
    print (my_issubset)
    my_issuperset = my_set101.issuperset(common_set2)
    print(my_issuperset)
    my_issubset2 = common_set3.issubset(my_set101)
    print (my_issubset2)

    print("")
    print("- set 2 list")
    big_set = my_set101.union(my_set102, my_set103)
    my_list3 = list(big_set)
    print(my_list3)

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

def examples_commandline():
    log_trace("examples_commandline")
    arg_count = len(sys.argv)

    ii = 0
    while ii < arg_count:
        print(str(ii) + ": " + sys.argv[ii])
        ii += 1

    if ii == 0:
        print ("zero")
    return

def TESTGRP_fileio():
    examples_fileio()
    examples_commandline()
    return

# ========================= main
# basics
#print ("Hello, World!\n")
#examples_string()
TESTGRP_string_methods()
#examples_number()
#examples_input()
#examples_if()
#examples_loop()
#examples_tryexcept()
#examples_func("jack", "pirate")
#print("cube is: {0}".format(str(examples_func2(3))))

# data structs
#examples_list()
#examples_tuple()
#examples_dict()
#examples_set()

# fileio
#TESTGRP_fileio()






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




# ========================= main
examples_set()







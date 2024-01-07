
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




# ========================= main

# data structs
examples_list()








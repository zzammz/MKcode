
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

def examples_misc_funcs():
    log_trace("examples_string")

    print("- divmod")
    res = divmod(7,2)
    print (res)

    print("- eval")
    #xx = 'print(55)'
    #eval(xx)

    print("- range 1")
    x2 = range(6)
    print (x2)
    x3 = range(2, 6)
    print (x3)

    print("- range 2")
    x4 = range (1, 10, 2)
    print (x4)
    ii = 0
    for ii in x4:
        print (ii)

    print("- round")
    print (round(5.567, 2))

    print("- sum")
    x5 = [1, 2, 3, 4, 5]
    print (sum(x5))
    print (sum(x5, 2))
    return



def examples_enum():
    fruits = ["apple", "banana", "orange"]
    for idx, val in enumerate(fruits):
        print ("index: {}  fruit: {}".format(idx, val))

    lang = "Python"
    for idx, ch in enumerate(lang):
        print ("idx:{}  ch:{}".format(idx, ch))
    return



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

def examples_substr():
    log_trace("examples_substr")

    print("")
    print("- basic substr")
    #string[start:end:step]
    test_str = "hello darkness my old friend"
    str1 = test_str[1:5]
    #print (str1)
    print(test_str[1:])  # all from 1 to end
    print(test_str[1:5]) # from 1 to 4
    print(test_str[-5:]) # last 5 chars
    print (test_str[::2]) # get every other character

    print("")
    print("- find substr")
    if "llo" in test_str:
        print ("found substr")
    if(test_str.find("XX") == -1):
        print ("not found")
    else:
        print ("not found")

    icount = test_str.count("e")
    print ("count of 'e' in string: " + str(icount))

    print("")
    print("- indexes of all occurrence")
    list2 = []
    my_string = "hello darkness my old friend"
    my_sub_string = "e"
    len_my_string = len(my_string)
    my_index = 0

    while my_index < len_my_string:
        tmp_index = my_string.find(my_sub_string, my_index)
        if tmp_index == -1:
            break
        list2.append(tmp_index)
        my_index = tmp_index + 1
    print (list2)

    print("")
    print("- substr through slicing")
    # Initialise the string
    fullstr = 'substring in python'
    print("Initial string: ", fullstr)

    # creating substring from beginning
    # define upto what index substring is needed
    istart = fullstr[:2]
    iend = fullstr[3:]
    # result
    print("Resultant substring from start:", istart)
    print("Resultant substring from end:", iend)

    print("")
    print("- substr through gap")
    # Create a substring by taking characters from a particular gap (step)
    # Initialise string
    fullstr = 'substring in python'
    print("Initial String: ", fullstr)
    # create substring by taking element after certain position gap and define length upto which substring is required
    alt = fullstr[::2]
    gap = fullstr[::3]

    #  Create a substring while considering string from the middle with some step gap between characters
    print("")
    print("- substr through middle and some gap")
    # Initialise string
    string = 'substring in python'
    print("Initial string: ", string)
    # create substring by taking element after certain step gap in a defined length
    astring = string[2:11:2]
    # result
    print("Resultant substring:", astring)
    # result
    print("Resultant substring from start:", alt)
    print("Resultant substring from end:", gap)

    print("")
    print("- all substring from start")
    test_str = "Geeks"
    for ictr in range (0, len(test_str)):
        test_substring = test_str[ictr:len(test_str)]
        print (test_substring)

    print("")
    print("- overlapping substr")
    fullstr = "GeeksforGeeksforGeeksforGeeks"
    teststr = "GeeksforGeeks"
    count_str = 0
    start_pos = 0
    while start_pos < len(fullstr):
        post_str_found = fullstr.find(teststr, start_pos)
        if post_str_found == -1:
            break
        else:
            count_str += 1
        start_pos = post_str_found + 1
    print ("count of overlapping str: " + str(count_str))

    return


def TESTGRP_string_methods():
    examples_string()
    str2 = "hello darkness my old friend"
    check_vowel_count(str2)
    check_exact_str()
    check_str_content()
    examples_substr()
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


# ---- funcs
def examples_func(name1, name2):
    print("hello to {0} and {1}".format(name1, name2))
    return

def examples_func2(num):
    return num * num * num


# =========== data structures: list, tuples, sets
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

# ========================= algorithms
# ------ fibonacci

# fibonacci
def fib_iterative(param_val):
    log_trace("fib_iterative")
    if param_val < 0:
        print ("incorrect value - cannot be less than 1")
        return

    prev_val = 0
    current_val = 1

    print(" {} ".format(0))
    if param_val == 1:
        return

    print(" {} ".format(1))
    if param_val == 2:
        return

    prev_val = current_val
    very_prev_val = 0

    for ictr in range (2, param_val):
        current_val = very_prev_val + prev_val
        very_prev_val = prev_val
        prev_val = current_val
        print (" {} ".format(current_val))
    return

def fib_recursive(param_val):
    log_trace("fib_recursive")
    if param_val < 0:
        print("incorrect value - cannot be less than 1")
        return
    elif param_val == 1:
        return 0
    elif param_val == 2:
        return 1
    else:
        return fib_recursive(param_val-1) + fib_recursive(param_val-2)


def TEST_fibonacci():
    log_trace("TEST_fibonacci")
    fib_iterative(5)
    print ("===")
    print ("{}th fib num is: ".format(5) + str(fib_recursive(5)))
    return



def sub_if_pwd_valid(param_sub_str):
    count_alpha = 0
    count_num = 0

    for cctr in range (0, len(param_sub_str)):
        if param_sub_str[cctr].isalpha():
            count_alpha += 1
        elif param_sub_str[cctr].isdigit():
            count_num += 1
        else:
            return -1

    if count_alpha > 0 and count_num > 0:
        if count_alpha % 2 == 0 and count_num %2 != 0:
            return count_alpha + count_num

    return -1


def demo_test(A):
    len_array = len(A)
    B = set(A)
    A2 = list(B)
    A2.sort()
    #if A2[0] != 1:
    #    return 1
    print (A2)
    for ictr in range(0, len_array):
        #print ("{}  {} ".format(A2[ictr], ictr+1))
        if A2[ictr] != ictr + 1:
            return ictr + 1
    return len_array+1

def demo_test2(A):
    len_array = len(A)
    A.sort()
    prev_val = 0
    ictr = 0
    for ictr in range(0, len_array):
        current_val = A[ictr]
        diff_val = current_val - prev_val
        if current_val < 1:
            continue
        if diff_val == 1:
            prev_val = current_val
            continue
        if diff_val > 1:
            return prev_val + 1
    if current_val < 1:
        return 1
    return current_val+1


def TEST_demo_test():
    ar1 = [1, 3, 1, 4]
    print (str(ar1) + " ... " + str(demo_test2(ar1)))

    ar1 = [1, 3, 6, 4, 1, 2]
    print (str(ar1) + " ... " + str(demo_test2(ar1)))

    ar1 = [-1, -3]
    print (str(ar1) + " ... " + str(demo_test2(ar1)))

    ar1 = [1, 2, 3]
    print (str(ar1) + " ... " + str(demo_test2(ar1)))

    ar1 = [-1, -1000, -20, 3]
    print (str(ar1) + " ... " + str(demo_test2(ar1)))

    ar1 = [1, -1, 2, 3, 5, 7, 9]
    print (str(ar1) + " ... " + str(demo_test2(ar1)))

    ar1 = [-1, 1, 2, 3]
    print (str(ar1) + " ... " + str(demo_test2(ar1)))

    ar1 = [-1, 4, 2, 3]
    print (str(ar1) + " ... " + str(demo_test2(ar1)))

    return

# --------------- find dupes

def FindDupes (p_array):
    log_trace("FindDupes")
    dupe_response = -1
    ictr = 0
    jctr = 0
    len_array = len(p_array)
    for ictr in range (0, len_array-1):
        for jctr in range (ictr+1, len_array):
            if p_array[ictr] == p_array[jctr]:
                dupe_response = p_array[ictr]
                return dupe_response

    return dupe_response


def FindDupes2 (p_array):
    log_trace("FindDupes2")
    p_array.sort()
    len_array = len(p_array)
    if len_array <= 1:
        return -1
    ictr = 0
    for ictr in range (0, len_array-1, 1):
        if p_array[ictr] == p_array[ictr+1]:
            return p_array[ictr]
    return -1


def TEST_FindDupes():
    test_array = [11, 13, 7, 11, 1, 3, 8, 4]
    response_dupe_check = FindDupes(test_array)
    if response_dupe_check == -1:
        print("No duplicates were found")
    else:
        print("Duplicate number: " + str(response_dupe_check))

    response_dupe_check = FindDupes2(test_array)
    if response_dupe_check == -1:
        print("No duplicates were found")
    else:
        print("Duplicate number: " + str(response_dupe_check))

    return



# ----------------- movies on flight
def MoviesOnFlight(p_array, p_duration, p_max_gap):
    log_trace("MoviesOnFlight")
    p_array.sort(reverse=True)
    for ictr in range (0, len(p_array)-1, 1):
        time_spent = p_duration - p_array[ictr] - p_array[ictr+1]
        if time_spent > 0 and time_spent <= p_max_gap:
            print(p_duration - p_array[ictr] - p_array[ictr+1])
            print ("[" + str(p_array[ictr]) + ", " + str(p_array[ictr+1]) + "]")
            return

    print ("Could not find 2 movies to watch within the " + str(p_duration) + " time period")
    return


def TEST_MoviesOnFlight():
    movie_array = [90, 85, 75, 60, 120, 150, 125]
    flight_duration = 250
    max_gap_allowed = 30
    MoviesOnFlight(movie_array, flight_duration, max_gap_allowed)
    return

# ----------------- push zeroes to end
def PushZeroesToEnd(p_array):
    log_trace("PushZeroesToEnd")
    print ("input array: " + str(p_array))
    len_array = len(p_array)
    for ictr in range (0, len_array, 1):
        if(p_array[ictr] == 0):
            for jctr in range (ictr, len_array-1, 1):
                p_array[jctr] = p_array[jctr+1]
            p_array[jctr+1] = 0
    print("output array: " + str(p_array))
    return

def TEST_PushZeroestoEnd():
    test_array = [1, 2, 0, 4, 3, 0, 5, 0]
    #test_array = [1, 0, 3, 5, 0]
    PushZeroesToEnd(test_array)
    return




# ========================= main
# basics
#print ("Hello, World!\n")
#examples_enum()
#examples_string()
#examples_misc_funcs()
#TESTGRP_string_methods()
#examples_number()
#examples_input()
#examples_if()
#examples_loop()
#examples_tryexcept()
#examples_func("jack", "pirate")
#print("cube is: {0}".format(str(examples_func2(3))))
#examples_datetime()

# data structs
#examples_list()
#examples_tuple()
#examples_dict()
#examples_set()

# fileio
#TESTGRP_fileio()

#DS_queue()
#DS_stack()

# algos
TEST_fibonacci()
TEST_FindDupes()
TEST_MoviesOnFlight()
TEST_PushZeroestoEnd()






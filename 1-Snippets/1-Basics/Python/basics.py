
# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

#https://www.w3schools.com/python/python_ref_string.asp
#https://www.afternerd.com/blog/python-enumerate/
# https://www.w3schools.com/css/default.asp
#https://www.geeksforgeeks.org/python-strings/
#https://www.geeksforgeeks.org/regular-expressions-python-set-1-search-match-find/
#https://rafal.io/archives.html
#https://regexr.com/


import inspect

def log_trace(func_name):
    print ("\n--- " + func_name)
    #print (inspect.stack()[1][3])
    #frame = inspect.currentframe()
    #print (inspect.getframeinfo(frame).function)
    #print(inspect.getframeinfo(inspect.currentframe()).function)
    return

#----------------- basics
import sys
from math import *

from pathlib import Path


def examples_string():
    char_name = "John"
    char_age = "40"
    print("cust_name " + char_name.upper() + " was only " + char_age)

    print(char_name.isupper())
    print(len(char_name))
    print(char_name[0])
    print(char_name.index("o"))
    print(char_name.replace("J", "GG"))
    return

def examples_numbers():
    my_num = 20
    print (my_num)
    print ("my number is " + str(my_num))
    my_num = 3.7
    print(round(my_num))

    return

def examples_input():
    #your_name = input("your name: ")
    #print ("you entered [" + your_name + "]")

    num1 = input ("enter num 1: ")
    num2 = input ("enter num 2: ")
    result = float(num1) + float(num2)
    print ("addition: " + str(result))
    return

def examples_madlib():
    my_color = input ("Enter color: ")
    my_noun = input("Enter noun: ")
    my_celebrity = input("Enter celebrity: ")

    print ("Roses are " + my_color)
    print (my_noun + " are blue")
    print ("I love " + my_celebrity)
    return

def examples_lists():
    friends_list = ["tim", "jack", "jim", "oscar", "coolio"]
    print (friends_list[1:3])
    print (friends_list[-1])
    friends_list[1] = "mike"
    print(friends_list[1:3])
    return

def examples_list_funcs():
    lucky_nums = [12, 8, 4, 16, 20, 24]
    friends_list = ["tim", "jack", "jim", "oscar", "steve", "rodney"]
    print (friends_list)
    friends_list.extend(lucky_nums)
    print(friends_list)
    friends_list.append("mandy")
    print(friends_list)
    friends_list.insert(1, "kelly")
    print(friends_list)
    friends_list.remove("oscar")
    print(friends_list)
    #friends_list.clear()
    friends_list.pop()
    print(friends_list)
    print(friends_list.index("jim"))
    print (friends_list.count("jim")) #count how many "jim" are there
    lucky_nums.sort()
    print(lucky_nums)
    lucky_nums.reverse();
    print(lucky_nums)
    lucky_nums2 = lucky_nums.copy()
    print (lucky_nums2)
    return

def examples_tuples():
    my_coords = (4, 5)
    print (my_coords[0])
    my_coords_list = [ (4,5), (45,67), (11, 22)]
    print (my_coords_list[1])
    print(my_coords_list[1][0])
    return

def examples_funcs(hello_name, hello_when):
    print ("Hello " + hello_name + " on", hello_when)
    return

def examples_cube (num):
    return num * num * num

def examples_if():
    is_male = False
    if is_male:
        print ("male")
    else:
        print ("female")

    is_tall = True
    if is_male and is_tall:
        print ("you are both male and tall")
    elif is_male and not(is_tall):
        print ("you are a short male")
    elif not(is_male) and is_tall:
        print ("you are a tall female")
    elif is_male or is_tall:
        print ("you are either male or tall")
    else:
        print ("diff combination")


    num1 = 1
    num2 = 1
    if num1 == num2 :
        print ("both num are equal")
    else :
        print ("not equal")
    return

def examples_dict():
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
    print(my_dict.get("Oct2"))
    print(my_dict.get("Oct2", "Not a valid key"))
    return

def examples_loop():
    i = 1
    while i<= 4:
        print (i)
        i += 1

    for letter in "Jacky":
        print (letter)

    friends = ["jim", "karen", "pam"]
    for friend in friends:
        print (friend)

    for ii in range (2):
        print (ii)

    for ii in range (len(friends)-1):
        print(friends[ii])

    return

def examples_listoflists():
    num_grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0]
    ]
    #print (num_grid[1][1])
    for row in num_grid:
        #print(row)
        for col in row:
            print (col)
    return

def examples_translate(phrase): #translate vowels into 'g'
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

def examples_translate_main():
    my_phrase = input ("enter a phrase to translate: ")
    response = examples_translate(my_phrase)
    print (response)
    return

# catch broad errors with just 'except'
# or catch specific errors with specific error codes
def examples_catch() :
    global_err = ""
    try:
        num = int (input("enter a number: "))
        print (num)
    except ZeroDivisionError as my_err: # for testing only - multiple except
        global_err = my_err
        print ("divided by zero")
    except ValueError as my_err:
        global_err = my_err
        print ("invalid input")
    except:
        print ("broad exception")
    print ("error: " + str(global_err))
    return

def examples_file_read() :
    file_emp = open("employees.txt", "r")
    #print(file_emp.readable())  # check if it is readable
    #print(file_emp.read()) # read entire file

    #print(file_emp.readline())  # read line & move to next line

    #print(file_emp.readlines())  # read lines & add to an array
    #print(file_emp.readlines()[1])  # read 2nd line from the array

    for emp in file_emp.readlines():
        print (emp)

    file_emp.close()
    return

def examples_file_append() :
    file_emp = open ("employees.txt", "a")
    file_emp.write("Kelly - Customer Service\n")
    file_emp.close()

    return

def examples_file_write () :
    file_emp = open ("employees2.txt", "w")
    file_emp.write ("Dave - Boss\n")
    file_emp.close()
    return



def examples_path() :
    path = Path ("C:\MKdocs\Dev\Python\one")
    print (path.exists())
    for file in path.glob("*.py"):
        print (file)
    return


def examples_commandline():
    arg_count = len(sys.argv)

    ii = 0
    while ii < arg_count:
        print(str(ii) + ": " + sys.argv[ii])
        ii += 1

    if ii == 0: print ("zero")

    return



#------------
import statistics

def mode_check(test_array):
    log_trace(inspect.getframeinfo(inspect.currentframe()).function)
    array_len = len(test_array)
    half_array_len = array_len // 2
    mode_number = -1
    try:
        mode_number = statistics.mode(test_array)
    except:
        return -1
    if mode_number > half_array_len:
        return mode_number
    else:
        return -1
    return -1

def TEST_mode_check():
    log_trace(inspect.getframeinfo(inspect.currentframe()).function)
    array1 = [5, 5, 5, 5, 8]
    response1 = mode_check(array1)
    print ("leader check value: " + str(response1))
    return



#---------------
def check_vowel(test_str):
    log_trace(inspect.getframeinfo(inspect.currentframe()).function)
    vowel_list = "AEIOUaeiou"
    vowel_count = 0
    for ii in range (0, len(test_str), 1):
        if test_str[ii] in vowel_list:
            vowel_count += 1
    print ("vowel count: " + str(vowel_count))

    return

def TEST_check_vowel():
    log_trace(inspect.getframeinfo(inspect.currentframe()).function)
    str2 = "HEllo darkness"
    check_vowel(str2)
    return

#----
def check_anagram(check_str1, check_str2):
    log_trace(inspect.getframeinfo(inspect.currentframe()).function)
    if sorted(check_str1) == sorted(check_str2):
        print ("string are anagrams")
    else:
        print ("strings are not anagrams")
    return

def TEST_check_anagram():
    log_trace(inspect.getframeinfo(inspect.currentframe()).function)
    str1 = "bad"
    str2 = "dad"
    check_anagram(str1, str2)

    str1 = "silent"
    str2 = "listen"
    check_anagram(str1, str2)

    return


def TEST_str_methods():
    log_trace(inspect.getframeinfo(inspect.currentframe()).function)
    str1 = "hello darkness"
    #print (str1.capitalize())
    #print (str1.center(30))
    #print (str1.count("e"))
    #print (str1.endswith("e"))
    #print (str1.find("e"))
    #print (str1.rfind("e"))
    #print (str1.find("e", 5, 11))
    #txt1 = "my name is {fname} and age {fage}".format(fname = "jack", fage=10)
    #print (txt1)
    #txt2 = "my name is {0} and age is {1}".format("Jack", 15)
    #print (txt2)
    #txt3 = "my name is {} and age is {}".format("jack", 17)
    #print (txt3)

    #str2 = "Hello123"
    #print(str2.isalnum())
    #print(str2.isalpha())

    #str3 = "234"
    #print (str3.isdecimal())

    #tuples
    #myTuple = ("one", "two", "three")
    #strTuple = "#".join(myTuple)
    #print (strTuple)
    #str5 = "I can eat many grapes in a day"
    #print (str5.partition("grapes"))

    #list
    #str6 = "I like apples"
    #print (str6.replace("apples", "mangoes"))
    #str7 = "welcome to the jungle"
    #print (str7.split())


    # trim spaces
    str4 = "     banana   "
    print ("[" + str4.lstrip() + "]")
    print ("[" + str4.rstrip() + "]")
    print ("[" + str4.lstrip().rstrip() + "]")

    str8 = "57"
    print (str8.zfill(7))

    return

def TEST_misc_funcs():
    res = divmod(5,2)
    print (res)

    xx = 'print(55)'
    eval(xx)

    x2 = range(6)
    print (x2)
    x3 = range(2, 6)
    print (x3)

    x4 = range (1, 10, 2)
    print (x4)
    ii = 0
    for ii in x4:
        print (ii)

    print (round(5.567, 2))

    x5 = [1, 2, 3, 4, 5]
    print (sum(x5))
    print (sum(x5, 2))

    return

# count substr plus any overlapping substr
def count_overlapping_substr(test_str, test_substring):
    count_str = 0
    start_pos = 0
    while start_pos < len(test_str):
        pos_str_found = test_str.find(test_substring, start_pos)
        if pos_str_found == -1:
            return count_str # not found
        else:
            count_str += 1
        start_pos = pos_str_found + 1
    return count_str

def TEST_count_overlapping_substr():
    teststr1 = "GeeksforGeeksforGeeksforGeeks"
    testsubstr1 = "GeeksforGeeks"
    print("count of overlapping str: " + str(count_overlapping_substr(teststr1, testsubstr1)))
    return


def get_all_substr(test_str):
    for ii in range(0, len(test_str)):
        test_substring = test_str[ii:len(test_str)]
        print (test_substring)
    return

def TEST_get_all_substr():
    get_all_substr("Geeks")
    return


# ----- date time
import datetime

def TEST_date_time():
    dt_obj = datetime.datetime.now()
    print (dt_obj)
    print (dt_obj.month)
    return

def queue_struct():
    fruits = []
    fruits.append("apple")
    fruits.append("banana")
    fruits.append("mango")
    print (fruits)
    print(fruits.pop(0))
    print(fruits)
    fruits.append("cherry")
    print(fruits)
    print(fruits.pop(0))
    print(fruits)

    return

# fibonacci
def fib_1(param_val):
    log_trace(inspect.getframeinfo(inspect.currentframe()).function)
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

def fib_2(param_val):
    #log_trace(inspect.getframeinfo(inspect.currentframe()).function)
    if param_val < 0:
        print("incorrect value - cannot be less than 1")
        return
    elif param_val == 1:
        return 0
    elif param_val == 2:
        return 1
    else:
        return fib_2(param_val-1) + fib_2(param_val-2)


def TEST_fib():
    fib_1(5)
    print ("===")
    print ("{}th fib num is: ".format(5) + str(fib_2(5)))
    return


def set_methods():
    show_fruit_examples = False
    if show_fruit_examples:
        fruits = {"apple", "banana", "cherry"}
        print(fruits)

        fruits.add("orange")
        print(fruits)

        fruits.update( ["apple", "mango", "banana"])
        print(fruits)
        print (len(fruits))

        fruits.discard("cherry")
        print(fruits)

        fruits.pop()
        print(fruits)

        if "apple" in fruits:
            print ("apple is a fruit")

    # create a set from values
    myset = set (("carrots", "cilantro"))
    print (myset)

    # create a set from array
    array2 = ["shoe", "sock"]
    print (array2)
    myset2 = set(array2)
    print (myset2)

    #check intersection of 2 or more sets
    ar1 = ["car", "bike", "helmet"]
    ar2 = ["bicycle", "helmet", "airpump"]
    ar3 = ["taekowndo", "dojo", "helmet"]

    sar1 = set (ar1)
    sar2 = set (ar2)
    sar3 = set (ar3)

    common_set2 = sar1.intersection(sar2)
    print (common_set2)

    common_set3 = sar1.intersection(sar2, sar3)
    print (common_set3)

    # check if subset
    res2 = sar1.issubset(sar2)
    print (res2)
    res3 = sar1.issuperset(common_set2)
    print (res3)
    res4 = common_set2.issubset(sar1)
    print (res4)

    big_set = sar1.union(sar2, sar3)
    print (big_set)

    # set to array/list
    ar5 = list (big_set)
    print (ar5)
    return

def TEST_try_except():
    #xx=1
    try:
        print (xx)
    except NameError:
        print ("variable xx not defined")
    except:
        print ("something else went wrong")
    else:
        print ("nothing went wrong")
    finally:
        print ("executing this whether error or not")
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



def TEST_ex():
    aa = "test"
    if aa[0].isalpha():
        print ("yes")
    return

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



def TEST_enum():
    fruits = ["apple", "banana", "orange"]
    for idx, val in enumerate(fruits):
        print ("index: {}  fruit: {}".format(idx, val))

    lang = "Python"
    for idx, ch in enumerate(lang):
        print ("idx:{}  ch:{}".format(idx, ch))
    return

# ------------------
def PrintMe(p_msg):
    print ("\n... " + p_msg + "()")
    return

def FindDupes (p_array):
    PrintMe("FindDupes")
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
    PrintMe("FindDupes2")
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

def MoviesOnFlight(p_array, p_duration, p_max_gap):
    PrintMe("MoviesOnFlight")
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

def PushZeroesToEnd(p_array):
    PrintMe("PushZeroesToEnd")
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

def TEST_dict():
    mydict = {
        "brand" : "Ford",
        "model" : "Mustabg",
        "year" : 1964,
        "type" : {
                "speed" : "Four",
                "race" : "Shelby"
        }
    }
    print (mydict)
    xx = mydict["model"]
    print (xx)
    mydict["color"] = "red"
    mydict["year"] = 2019
    print(mydict)
    for (x,y) in mydict.items():
        print(x, y)
    return


# ------ main
#check_time_spent()
#log_trace(inspect.getframeinfo(inspect.currentframe()).function)
#TEST_str_methods()
#TEST_misc_funcs()
#TEST_check_vowel()
#TEST_check_anagram()
#TEST_count_overlapping_substr()
#TEST_get_all_substr()
#TEST_FindDupIntInArray()
#TEST_student_class()
#TEST_chef_class()
#TEST_remove_dupes_from_list()
#TEST_json()
#TEST_date_time()
#queue_struct()
#TEST_fib()
#set_methods()
#TEST_try_except()
#TEST_ex()
#TEST_demo_test()
#TEST_enum()
#check_time_spent2()

print ("Hello, World!\n")
#examples_string()
#examples_numbers()
#examples_input()
#examples_madlib()
#examples_lists()
#examples_list_funcs()
#examples_tuples()
#examples_funcs("paul", "today")
#print(examples_cube(4))
#examples_if()
#examples_dict()
#examples_loop()
#examples_listoflists()
#examples_translate_main()
#examples_catch()
#examples_file_append()
#examples_file_read()
#examples_file_write()

#run_test(questions)

#examples_path()
examples_commandline()


#TEST_FindDupes()
#TEST_MoviesOnFlight()
#TEST_PushZeroestoEnd()
#TEST_dict()



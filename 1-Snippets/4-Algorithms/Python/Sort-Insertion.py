


#------------------
#------------------


def insertion_sort (param_array):

    for ictr in range (len(param_array)):
        my_cursor = param_array[ictr]
        my_pos = ictr

        while my_pos > 0 and param_array[my_pos - 1] > my_cursor:
            param_array[my_pos] = param_array[my_pos - 1]
            my_pos = my_pos - 1
        param_array[my_pos] = my_cursor

    return param_array



#---------------
def TEST_sortmethods():

    array3 = orig_array.copy()
    print ("array3: " + str(array3))
    ret_array = insertion_sort(array3)
    print ("insertion sorted: " + str(ret_array))

    print ()

    return


#--------------------------
# version 2
#--------------------------

def insertion_sort2(p_array):

    len_array = len(p_array)
    for ictr in range (0, len_array):
        my_cursor = p_array[ictr]
        mypos = ictr

        while mypos > 0 and p_array[mypos-1]>my_cursor:
            p_array[mypos] = p_array[mypos-1]
            mypos -= 1
        p_array[mypos] = my_cursor

    return p_array


#---------------
def TEST_sortmethods2():

    array1 = orig_array.copy()
    print ("array1: " + str(array1))
    ret_array = insertion_sort2(array1)
    print ("insertion_sort2 " + str(ret_array))

    return

#------------
#    version2
# -------------

def insertion_sort3(p_array):
    len_array = len(p_array)
    for ictr in range(0, len_array):
        mycursor = p_array[ictr]
        mypos = ictr
        while mypos>0 and p_array[mypos-1]>mycursor:
            p_array[mypos] = p_array[mypos-1]
            mypos -= 1
        p_array[mypos] = mycursor
    return p_array


#---------------
def TEST_sortmethods3():
    orig_array = [3, 5, 7, 9, 10, 4, 2, 1, 8, 6]

    array1 = orig_array.copy()
    print ("array1: " + str(array1))
    ret_array = insertion_sort3(array1)
    print ("insertion_sort3 " + str(ret_array))

    return



#--------- main
TEST_sortmethods()
TEST_sortmethods2()
TEST_sortmethods3()


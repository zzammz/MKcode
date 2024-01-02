

#------------------

def bubble_sort (param_array):

    def swap (i, j):
        param_array[i], param_array[j] = param_array[j], param_array[i]
        return

    len_array = len(param_array)
    is_swapped = True
    x = -1
    while is_swapped:
        is_swapped = False
        x += 1
        for ictr in range(1, len_array-x):
            if param_array[ictr-1] > param_array[ictr]:
                swap (ictr-1, ictr)
                is_swapped = True

    return param_array




#---------------
def TEST_sortmethods():
    orig_array = [3, 5, 7, 9, 10, 4, 2, 1, 8, 6]

    array1 = orig_array.copy()
    print ("array1: " + str(array1))
    ret_array = bubble_sort(array1)
    print ("bubble sorted: " + str(ret_array))

    print ()


#--------------------------
# version 2
#--------------------------
def bubble_sort2_rev(p_array):

    def swap (i, j):
        p_array[i], p_array[j] = p_array[j], p_array[i]
        return

    len_array = len(p_array)
    xfactor = -1
    is_swapped = True;
    while is_swapped:
        is_swapped = False
        xfactor += 1
        for ictr in range (1, len_array-xfactor):
            if p_array[ictr-1] < p_array[ictr]:
                swap (ictr-1, ictr)
                is_swapped = True
    return p_array


def bubble_sort2(p_array):
    def swap(i, j):
        p_array[i], p_array[j] = p_array[j], p_array[i]
        return

    len_array = len(p_array)
    is_swapped = True
    x = -1
    while is_swapped:
        is_swapped = False
        x += 1
        for ictr in range (1, len_array-x):
            if p_array[ictr-1] > p_array[ictr]:
                swap (ictr-1, ictr)
                is_swapped = True
    return p_array


#---------------
def TEST_sortmethods2():
    orig_array = [3, 5, 7, 9, 10, 4, 2, 1, 8, 6]

    array1 = orig_array.copy()
    print ("array1: " + str(array1))
    ret_array = bubble_sort2(array1)
    print ("bubble-2 sorted: " + str(ret_array))

    array1 = orig_array.copy()
    print ("array1: " + str(array1))
    ret_array = bubble_sort3(array1)
    print ("bubble-3 sorted: " + str(ret_array))

    return

    array1 = orig_array.copy()
    print ("array1: " + str(array1))
    ret_array = bubble_sort2_rev(array1)
    print ("bubble_sort2_rev: " + str(ret_array))


#------------
#    version2
# -------------


def bubble_sort4(p_array):
    def swap(i, j):
        p_array[i], p_array[j] = p_array[j], p_array[i]
        return

    len_array = len(p_array)
    xfactor = -1
    is_swapped = True
    while is_swapped:
        is_swapped = False
        xfactor +=1
        for ictr in range (1, len_array-xfactor):
            if p_array[ictr-1] > p_array[ictr]:
                swap(ictr-1, ictr)
                is_swapped = True
    return p_array



#---------------
def TEST_sortmethods3():
    orig_array = [3, 5, 7, 9, 10, 4, 2, 1, 8, 6]

    array1 = orig_array.copy()
    print ("array1: " + str(array1))
    ret_array = bubble_sort4(array1)
    print ("bubble-4 sorted: " + str(ret_array))

    return



#--------- main
TEST_sortmethods()
TEST_sortmethods2()
TEST_sortmethods3()


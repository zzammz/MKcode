


#------------------
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


def selection_sort (param_array):
    for ictr in range (len(param_array)):
        min_value = ictr

        for jctr in range (ictr+1, len(param_array)):
            if param_array[jctr] < param_array[min_value]:
                min_value = jctr

        param_array[min_value], param_array[ictr] = param_array[ictr], param_array[min_value]

    return param_array


def insertion_sort (param_array):

    for ictr in range (len(param_array)):
        my_cursor = param_array[ictr]
        my_pos = ictr

        while my_pos > 0 and param_array[my_pos - 1] > my_cursor:
            param_array[my_pos] = param_array[my_pos - 1]
            my_pos = my_pos - 1
        param_array[my_pos] = my_cursor

    return param_array

# ------
def Zpartition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def ZquickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = Zpartition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        ZquickSort(arr, low, pi - 1)
        ZquickSort(arr, pi + 1, high)
        return arr
        #print (arr)
    # -------

def Zquick_sort(param_array):
    my_start_array = 0
    my_end_array = len(param_array)-1

    return ZquickSort(param_array, my_start_array, my_end_array)



#---------------
def TEST_sortmethods():
    orig_array = [3, 5, 7, 9, 10, 4, 2, 1, 8, 6]

    array1 = orig_array.copy()
    print ("array1: " + str(array1))
    ret_array = bubble_sort(array1)
    print ("bubble sorted: " + str(ret_array))

    print ()

    array2 = orig_array.copy()
    print ("array2: " + str(array2))
    ret_array = selection_sort(array2)
    print ("selection sorted: " + str(ret_array))

    print ()

    array3 = orig_array.copy()
    print ("array3: " + str(array3))
    ret_array = insertion_sort(array3)
    print ("insertion sorted: " + str(ret_array))

    print ()

    array4 = orig_array.copy()
    print ("array4: " + str(array4))
    #ret_array = quick_sort(array4)
    #ret_array = Yquicksort(array4)
    ret_array = Zquick_sort(array4)
    print ("Zquick sorted: " + str(ret_array))
    return


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


def func_2(myval):
    if myval % 2 == 0:
        return None
    return myval

def func_1():
    if func_2(7) == None:
        print("None")
    else:
        print("something")
    return

#----- quick sort
def QuickSort_partition(p_array, p_low, p_high):
    ii = p_low - 1
    pivot = p_array[p_high]

    for jj in range(p_low, p_high):
        if p_array[jj] <= pivot:
            ii += 1
            p_array[ii], p_array[jj] = p_array[jj], p_array[ii]

    p_array[ii+1], p_array[p_high] = p_array[p_high], p_array[ii+1]
    return ii+1

def QuickSort_sub(p_array, p_low, p_high):
    if p_low < p_high:
        partition_index = QuickSort_partition(p_array, p_low, p_high)
        QuickSort_sub(p_array, p_low, partition_index-1)
        QuickSort_sub(p_array, partition_index+1, p_high)
        return p_array


def QuickSort_main(p_array):
    array_start = 0
    array_end = len(p_array)-1
    return QuickSort_sub(p_array, array_start, array_end)


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

    array1 = orig_array.copy()
    print ("array1: " + str(array1))
    ret_array = insertion_sort2(array1)
    print ("insertion_sort2 " + str(ret_array))

    array1 = orig_array.copy()
    print ("array1: " + str(array1))
    ret_array = QuickSort_main(array1)
    print ("QuickSort_main " + str(ret_array))
    return

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


#----- quick sort
def Quicksort_partition3(p_array, p_low, p_high):
    pivot = p_array[p_high]
    ii = p_low-1
    for jj in range (p_low, p_high):
        if p_array[jj] <= pivot:
            ii += 1
            p_array[ii], p_array[jj] = p_array[jj], p_array[ii]
    p_array[ii+1], p_array[p_high] = p_array[p_high], p_array[ii+1]
    return ii+1

def Quicksort_sub3(p_array, p_low, p_high):
    if p_low < p_high:
        partition_index = Quicksort_partition3(p_array, p_low, p_high)
        Quicksort_sub3(p_array, p_low, partition_index-1)
        Quicksort_sub3(p_array, partition_index+1, p_high)
        return p_array


def Quicksort_main3(p_array):
    array_start = 0
    array_end = len(p_array)-1
    return Quicksort_sub3(p_array, array_start, array_end)


#---------------
def TEST_sortmethods3():
    orig_array = [3, 5, 7, 9, 10, 4, 2, 1, 8, 6]

    array1 = orig_array.copy()
    print ("array1: " + str(array1))
    ret_array = bubble_sort4(array1)
    print ("bubble-4 sorted: " + str(ret_array))

    array1 = orig_array.copy()
    print ("array1: " + str(array1))
    ret_array = insertion_sort3(array1)
    print ("insertion_sort3 " + str(ret_array))


    array1 = orig_array.copy()
    print ("array1: " + str(array1))
    ret_array = Quicksort_main3(array1)
    print ("QuickSort_main3 " + str(ret_array))


    return



#--------- main
#print ("Hello, World!")
#conn = psycopg2.connect(database = "testdb", user = "postgres", password = "123", host = "127.0.0.1", port = "5432")
#TEST_sortmethods()

TEST_sortmethods3()
#func_1()

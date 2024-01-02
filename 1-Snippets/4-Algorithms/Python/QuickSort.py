


#------------------
#------------------

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
    ret_array = QuickSort_main(array1)
    print ("QuickSort_main " + str(ret_array))
    return

#------------
#    version2
# -------------

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
    ret_array = Quicksort_main3(array1)
    print ("QuickSort_main3 " + str(ret_array))


    return



#--------- main

TEST_sortmethods()
TEST_sortmethods2()
TEST_sortmethods3()

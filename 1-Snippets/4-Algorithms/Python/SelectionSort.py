

#------------------
#------------------

def selection_sort (param_array):
    for ictr in range (len(param_array)):
        min_value = ictr

        for jctr in range (ictr+1, len(param_array)):
            if param_array[jctr] < param_array[min_value]:
                min_value = jctr

        param_array[min_value], param_array[ictr] = param_array[ictr], param_array[min_value]

    return param_array



#---------------
def TEST_sortmethods():
    orig_array = [3, 5, 7, 9, 10, 4, 2, 1, 8, 6]

    print ()

    array2 = orig_array.copy()
    print ("array2: " + str(array2))
    ret_array = selection_sort(array2)
    print ("selection sorted: " + str(ret_array))

    print ()

    return


#--------- main

TEST_sortmethods()


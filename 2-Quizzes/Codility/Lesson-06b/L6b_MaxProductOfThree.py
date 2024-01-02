
# ==========
def L6b_MaxProductOfThree (p_array):
    p_array.sort()
    len_array = len(p_array)
    product3 = p_array[len_array-1] * p_array[len_array-2] * p_array[len_array-3]
    return product3



def TEST_L6b_MaxProductOfThree():
    array_1 = [-3, 1, 2, -2, 5, 6]
    print ("array={}  max product of three={}".format(array_1, L6b_MaxProductOfThree(array_1)))
    return




# =========== main
TEST_L6b_MaxProductOfThree()

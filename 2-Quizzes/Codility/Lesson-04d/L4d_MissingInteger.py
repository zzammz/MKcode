# ==========
def L4d_MissingInteger2 (p_array):
    p_array.sort()
    array_len = len(p_array)
    if max(p_array) != array_len:
        return 0

    for ictr in range (0, array_len):
        if p_array[ictr] == ictr+1:
            continue
        else:
            return 0
    return 1

def L4d_MissingInteger (p_array):
    p_array.sort()
    tmp_set = set (p_array)
    p2_array = list(tmp_set)
    #print (tmp_set)
    #print (p_array2)
    len_array = len(p2_array)
    if len_array == 0:
        return 1
    if p2_array[0] <= 0:
        return 1

    #for ictr in range (0, len_array)
    ictr = 0
    while ictr < len_array:
        if p2_array[ictr] != ictr+1:
            return ictr+1
        ictr += 1

    return len_array+1


def TEST_L4d_MissingInteger():
    array_1 = []
    print ("array={}  small missing int={}".format(array_1, L4e_MissingInteger(array_1)))

    array_1 = [4, 1, 3]
    print ("array={}  small missing int={}".format(array_1, L4e_MissingInteger(array_1)))

    array_1 = [4, 1, 3, 2, 1]
    print ("array={}  small missing int={}".format(array_1, L4e_MissingInteger(array_1)))

    return

# =========== main
TEST_L4d_MissingInteger()


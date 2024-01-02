# ==========
def L3b_PermMissingElem (p_array):
    p_array.sort()
    if len (p_array) == 0:
        return 1
    for ictr in range (0, len(p_array)):
        if p_array[ictr] != ictr+1:
            return ictr+1
    return -1


def TEST_L3b_PermMissingElem():
    array_1 = [2, 3, 1, 5]
    print ("array={}  missing element={}".format(array_1, L3b_PermMissingElem(array_1)))

    array_1 = []
    print ("array={}  missing element={}".format(array_1, L3b_PermMissingElem(array_1)))

    array_1 = [2, 3, 1, 4]
    print ("array={}  missing element={}".format(array_1, L3b_PermMissingElem(array_1)))

    return

# =========== main
TEST_L3b_PermMissingElem()

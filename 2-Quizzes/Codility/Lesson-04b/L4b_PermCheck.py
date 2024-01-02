# ==========
def L4b_PermCheck (p_array):
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


def TEST_L4b_PermCheck():
    array_1 = [4, 1, 3]
    print ("array={}  is permutation={}".format(array_1, L4b_PermCheck(array_1)))

    array_1 = [4, 1, 3, 2]
    print ("array={}  is permutation={}".format(array_1, L4b_PermCheck(array_1)))

    array_1 = [4, 1, 3, 2, 1]
    print ("array={}  is permutation={}".format(array_1, L4b_PermCheck(array_1)))

    return

# =========== main
TEST_L4b_PermCheck()


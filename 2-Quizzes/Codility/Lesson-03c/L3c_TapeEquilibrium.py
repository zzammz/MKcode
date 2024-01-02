# ==========
def L3c_TapeEquilibrium (p_array):
    print (p_array)
    full_sum = sum(p_array)
    min_diff_val = full_sum
    tmp_diff = 0
    left_side_sum = 0
    right_side_sum = full_sum
    for ictr in range (0, len(p_array)):
        left_side_sum = left_side_sum + p_array[ictr]
        right_side_sum = right_side_sum - p_array[ictr]
        tmp_diff = abs(left_side_sum - right_side_sum)
        min_diff_val = min(min_diff_val, tmp_diff)

    return min_diff_val


def TEST_L3c_TapeEquilibrium():
    array_1 = [3, 1, 2, 4, 3]
    print ("array={}  min diff={}".format(array_1, L3c_TapeEquilibrium(array_1)))

    return


# =========== main
TEST_L3c_TapeEquilibrium()

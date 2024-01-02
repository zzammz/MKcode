# ==========
def L2a_CyclicRotation(p_array, p_shift_count):
    jctr = 0
    while jctr < p_shift_count:
        tmpval = 0
        prev_val = p_array[0]
        for ictr in range (1, len(p_array)):
            this_val = p_array[ictr]
            p_array[ictr] = prev_val
            prev_val = this_val
            print (ictr)
            p_array[0] = prev_val
        jctr += 1
    return p_array

def TEST_L2a_CyclicRotation():
    array_1 = [1, 2, 3, 4]
    array_shift_count = 2
    print ("array={}  shift_count={}  shifted={}".format(array_1, array_shift_count, L2a_CyclicRotation(array_1, array_shift_count)))
    return

# =========== main
TEST_L2a_CyclicRotation()

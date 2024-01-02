# ==========
def L6a_Distinct (p_array):
    p_set = set (p_array)
    return len (p_set)



def TEST_L6a_Distinct():
    array_1 = [1, 2, 3, 4, 1, 2]
    print ("array={}  distinct count={}".format(array_1, L6a_Distinct(array_1)))
    return

# =========== main
TEST_L6a_Distinct()


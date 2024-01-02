# ==========
import statistics

def L8a_Dominator (p_array):
    mode_val = statistics.mode(p_array)
    count_val = p_array.count(mode_val)
    half_of_array = len(p_array) / 2
    if count_val > half_of_array:
        return mode_val
    return -1


def TEST_L8a_Dominator():
    array_1 = [1, 2, 3, 1, 4, 1, 5, 1, 1]
    print ("array={}  dominator={}".format(array_1, L8a_Dominator(array_1)))
    return

# =========== main
TEST_L8a_Dominator()


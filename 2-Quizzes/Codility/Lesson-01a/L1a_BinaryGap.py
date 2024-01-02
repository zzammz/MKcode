# ==========
def L1a_BinaryGap(param_num):
    #print ("--- L1a_BinaryGap: param={}".format(param_num))
    #num_bin - bin(param_num)
    param_num2 = bin(param_num)[2:]
    max_gap_count = 0
    zero_ctr = 0
    for tmpchar in param_num2:
        if tmpchar == "1":
            max_gap_count = max (zero_ctr, max_gap_count)
            zero_ctr = 0
            continue
        if tmpchar == "0":
            zero_ctr += 1
            continue

    max_gap_count = max (zero_ctr, max_gap_count)
    return max_gap_count


def TEST_L1a_BinaryGap():
    print ("--- TEST_L1a_BinaryGap")
    num_decimal = 104
    num_bin = bin(num_decimal)
    print ("decimal={}  binary={}  max_gap={}".format(num_decimal, num_bin, L1a_BinaryGap(num_decimal)))
    #L1a_BinaryGap(num_bin)
    return

# =========== main
TEST_L1a_BinaryGap()

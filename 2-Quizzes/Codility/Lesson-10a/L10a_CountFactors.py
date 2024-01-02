# ==========
def L10a_CountFactors (p_val):
    factors_list = []
    if p_val <= 0:
        return factors_list

    if p_val == 1:
        factors_list.append(1)
        return factors_list

    for ictr in range (1, p_val+1):
        if p_val % ictr == 0:
            factors_list.append(ictr)

    return factors_list



def TEST_L10a_CountFactors():
    val_1 = 24
    print ("value={}  factors={}".format(val_1, L10a_CountFactors(val_1)))
    return

# =========== main
TEST_L10a_CountFactors()


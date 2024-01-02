# ==========
def L10b_MinPerimeterRectangle (p_val):
    factors_list = []

    factors_list = L10a_CountFactors(p_val)
    min_rect_parameter = p_val * p_val
    tmp_rect_parameter = 0

    for ival in factors_list:
        factor_one = ival
        factor_two = int(p_val / factor_one)
        tmp_rect_parameter = 2 * factor_one + 2 * factor_two
        min_rect_parameter = min (min_rect_parameter, tmp_rect_parameter)

    return min_rect_parameter


def TEST_L10b_MinPerimeterRectangle():
    val_1 = 30
    print ("value={}  min parameter={}".format(val_1, L10b_MinPerimeterRectangle(val_1)))
    return

# =========== main
TEST_L10b_MinPerimeterRectangle()


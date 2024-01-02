# ==========

def L9a_MaxProfit (p_array):
    max_val = max(p_array)
    max_profit = 0
    for ictr in range (0, len(p_array)-1):
        buy_val = p_array[ictr]
        max_val = max (p_array[ictr+1:])
        max_profit = max(max_profit, max_val-buy_val)
        #print ("ictr={}  buy_val={}   max_val={}   max_profit={}".format(ictr, buy_val, max_val, max_profit))
    return max_profit


def TEST_L9a_MaxProfit():
    array_1 = [23171, 21011, 21123, 21366, 21013, 21367]
    print ("array={}  max profit={}".format(array_1, L9a_MaxProfit(array_1)))


# =========== main
TEST_L9a_MaxProfit()

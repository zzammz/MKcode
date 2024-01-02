 ==========
def L5b_CountDiv (A, B, K):
    div_count = 0
    ictr = A
    while ictr <= B:
        if ictr % K == 0:
            div_count += 1
        ictr += 1

    return div_count


def TEST_L5b_CountDiv():
    A = 6
    B = 11
    K = 2
    print ("A={}  B={}   K={}   response={}".format(A, B, K, L5b_CountDiv(A, B, K)))
    return

# =========== main
TEST_L5b_CountDiv()



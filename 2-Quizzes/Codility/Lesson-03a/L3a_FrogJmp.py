# ==========
def L3a_FrogJmp (p_xx, p_yy, p_dd):
    sum_val = p_xx
    jump_count = 0
    while True:
        sum_val = sum_val + p_dd
        jump_count += 1
        if sum_val > p_yy:
            return jump_count
        #jump_count += 1

    return -1

def TEST_L3a_FrogJmp():
    xx = 10
    yy = 85
    dd = 30
    print ("xx={}  yy={}  dd={}  jump count={}".format(xx, yy, dd, L3a_FrogJmp(xx, yy, dd)))

    xx = 2
    yy = 9
    dd = 3
    print ("xx={}  yy={}  dd={}  jump count={}".format(xx, yy, dd, L3a_FrogJmp(xx, yy, dd)))

    return

# =========== main
TEST_L3a_FrogJmp()

# ==========
def L2b_OddOccurrencesInArray (p_array):
    p_array.sort()
    ictr = 1
    item_count = 1
    prev_item = p_array[0]

    while ictr < len(p_array):
        this_item = p_array[ictr]
        #print ("[{}]: prev={}  this={}  count={}".format(ictr, prev_item, this_item, item_count))

        if this_item != prev_item:
            if item_count == 1:
                return prev_item
            item_count = 1
            prev_item = this_item
            ictr += 1
            continue
        else:
            prev_item = this_item
            item_count += 1
            ictr += 1
            continue

    return prev_item

def TEST_L2b_OddOccurrencesInArray():
    array_1 = [5, 8, 8, 5, 7, 3, 4, 3, 4]
    print ("array={}  odd number={}".format(array_1, L2b_OddOccurrencesInArray(array_1)))

    array_1 = [5, 7, 8, 5, 7, 3, 4, 3, 4]
    print ("array={}  odd number={}".format(array_1, L2b_OddOccurrencesInArray(array_1)))

    array_1 = [5, 2, 7, 7, 5, 7, 3, 4, 3, 4]
    print ("array={}  odd number={}".format(array_1, L2b_OddOccurrencesInArray(array_1)))

    return

# =========== main
TEST_L2b_OddOccurrencesInArray()


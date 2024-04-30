

import inspect
import sys

# ========================= common
def log_trace(func_name):
    print ("\n\n========== " + func_name + "()")
    #print (inspect.stack()[1][3])
    #frame = inspect.currentframe()
    #print (inspect.getframeinfo(frame).function)
    #print(inspect.getframeinfo(inspect.currentframe()).function)
    return

def log_trace2(str_msg):
    print ("\n--- " + str_msg)
    return


def set_basics():
    log_trace("set_basics")

    print ("")
    log_trace2("creating")

    # empty
    st = set()

    # creating with data
    st = {'item1', 'item2', 'item3', 'item4'}
    fruits = {'banana', 'orange', 'mango', 'lemon'}

    log_trace2("getting length")
    st = {'item1', 'item2', 'item3', 'item4'}
    print (st)
    print(len(st))
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    print (fruits)
    print(len(fruits))

    log_trace2("accessing items in a set")
    st = {'item1', 'item2', 'item3', 'item4'}
    print (st)
    print("Does set st contain item3? ", 'item3' in st)  # Does set st contain item3? True

    print ("")
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    print (fruits)
    print ("check of 'mango'")
    print('mango' in fruits)  # True

    return


def adding_items():
    log_trace("adding_items")

    log_trace2("add 1 item")
    st = {'item1', 'item2', 'item3', 'item4'}
    print (st)
    st.add('item5')
    print (st)

    fruits = {'banana', 'orange', 'mango', 'lemon'}
    print(fruits)
    fruits.add('lime')
    print(fruits)

    log_trace2("add multiple items using 'update'")
    st = {'item1', 'item2', 'item3', 'item4'}
    print (st)
    st.update(['item5', 'item6', 'item7'])
    print (st)

    fruits = {'banana', 'orange', 'mango', 'lemon'}
    vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
    print (fruits)
    fruits.update(vegetables)
    print (fruits)

    return


def removing_items():
    log_trace("removing_items")

    log_trace2("removing: using 'remove' to remove item2")
    st = {'item1', 'item2', 'item3', 'item4'}
    print (st)
    st.remove('item2')
    print(st)

    log_trace2("removing: using pop, which removes a random item")
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    print (fruits)
    fruits.pop()  # removes a random item from the set
    print(fruits)

    print ("")
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    print(fruits)
    removed_item = fruits.pop()
    print (removed_item)
    print (fruits)

    log_trace2("clearing items in a set")
    st = {'item1', 'item2', 'item3', 'item4'}
    print (st)
    st.clear()
    print(st)

    log_trace2("delete whole set")
    st = {'item1', 'item2', 'item3', 'item4'}
    del st
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    del fruits

    return


def convert_list_to_set():
    log_trace("convert_list_to_set")

    lst = ['item1', 'item2', 'item3', 'item4', 'item1']
    st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
    print (lst)
    print (st)

    fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
    set_fruits = set(fruits)  # {'mango', 'lemon', 'banana', 'orange'}
    print (fruits)
    print (set_fruits)

    return



def joining_sets():
    log_trace("joining_sets")

    log_trace2("using 'union'")
    st1 = {'item1', 'item2', 'item3', 'item4'}
    st2 = {'item5', 'item6', 'item7', 'item8'}
    st3 = st1.union(st2)

    fruits = {'banana', 'orange', 'mango', 'lemon'}
    vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
    print(fruits.union(vegetables))  # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

    log_trace2("using 'update'")
    st1 = {'item1', 'item2', 'item3', 'item4'}
    st2 = {'item5', 'item6', 'item7', 'item8'}
    st1.update(st2)  # st2 contents are added to st1

    fruits = {'banana', 'orange', 'mango', 'lemon'}
    vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
    fruits.update(vegetables)
    print(fruits)  # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

    log_trace2("finding intersection items")
    st1 = {'item1', 'item2', 'item3', 'item4'}
    st2 = {'item3', 'item2'}
    print (st1)
    print (st2)
    print ("intersection (common) items:")
    st4 = st1.intersection(st2)  # {'item3', 'item2'}
    print (st4)

    print ("")
    whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    even_numbers = {0, 2, 4, 6, 8, 10}
    whole_numbers.intersection(even_numbers)  # {0, 2, 4, 6, 8, 10}

    python = {'p', 'y', 't', 'h', 'o', 'n'}
    dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
    common_python_dragon = python.intersection(dragon)  # {'o', 'n'}
    print (python)
    print (dragon)
    print ("intersection items:")
    print (common_python_dragon)

    return


def checking_subset_superset():
    log_trace("checking_subset_superset")

    st1 = {'item1', 'item2', 'item3', 'item4'}
    st2 = {'item2', 'item3'}
    st2.issubset(st1)  # True
    st1.issuperset(st2)  # True

    whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    even_numbers = {0, 2, 4, 6, 8, 10}
    whole_numbers.issubset(even_numbers)  # False, because it is a super set
    whole_numbers.issuperset(even_numbers)  # True

    python = {'p', 'y', 't', 'h', 'o', 'n'}
    dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
    python.issubset(dragon)  # False

    return


def difference_between_sets():
    log_trace("difference_between_sets")

    st1 = {'item1', 'item2', 'item3', 'item4'}
    st2 = {'item2', 'item3'}
    st2.difference(st1)  # set()
    st1.difference(st2)  # {'item1', 'item4'} => st1\st2

    whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    even_numbers = {0, 2, 4, 6, 8, 10}
    whole_numbers.difference(even_numbers)  # {1, 3, 5, 7, 9}

    python = {'p', 'y', 't', 'o', 'n'}
    dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
    python_diff_dragon = python.difference(dragon)  # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
    print (python_diff_dragon)
    dragon_diff_python = dragon.difference(python)  # {'d', 'r', 'a', 'g'}
    print (dragon_diff_python)

    return


def symmetric_difference():
    log_trace("symmetric_difference")

    st1 = {'item1', 'item2', 'item3', 'item4'}
    st2 = {'item2', 'item3'}
    # it means (A\B)∪(B\A)
    st2.symmetric_difference(st1)  # {'item1', 'item4'}

    whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    some_numbers = {1, 2, 3, 4, 5}
    symm_diff = whole_numbers.symmetric_difference(some_numbers)  # {0, 6, 7, 8, 9, 10}
    print (symm_diff)

    python = {'p', 'y', 't', 'h', 'o', 'n'}
    dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
    symm_diff2 = python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
    print (symm_diff2)

    return


def disjointed_sets():
    log_trace("disjointed_sets")

    st1 = {'item1', 'item2', 'item3', 'item4'}
    st2 = {'item2', 'item3'}
    is_disjoint1 = st2.isdisjoint(st1)  # False
    print (is_disjoint1)

    even_numbers = {0, 2, 4, 6, 8}
    odd_numbers = {1, 3, 5, 7, 9}
    is_disjoint2 = even_numbers.isdisjoint(odd_numbers)  # True, because no common item
    print(is_disjoint2)

    python = {'p', 'y', 't', 'h', 'o', 'n'}
    dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
    is_disjoint3 = python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
    print(is_disjoint3)

    return



def setDisp(**kwargs):
    log_trace("xx")

    # kwargs is a dict
    print(type(kwargs))

    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))

    return

# ========================= main
set_basics()
adding_items()
removing_items()
convert_list_to_set()
joining_sets()
checking_subset_superset()
difference_between_sets()
symmetric_difference()
disjointed_sets()


# Driver code
#setDisp(name="geeks", ID="101", language="Python")

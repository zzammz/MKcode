

import inspect
import sys

# ========================= common
def log_trace(func_name):
    print ("\n----- " + func_name + "() -----")
    #print (inspect.stack()[1][3])
    #frame = inspect.currentframe()
    #print (inspect.getframeinfo(frame).function)
    #print(inspect.getframeinfo(inspect.currentframe()).function)
    return



def tuples_basics():
    log_trace("tuples_basics")

    print ("")
    print ("-- creating")

    # syntax
    empty_tuple = ()
    print(empty_tuple)

    # or using the tuple constructor
    empty_tuple = tuple()
    print (empty_tuple)

    tpl = ('item1', 'item2', 'item3')
    print (tpl)
    fruits = ('banana', 'orange', 'mango', 'lemon')
    print (fruits)

    print("")
    print("-- tuple length")
    print("length of tpl: " + str(len(tpl)) )
    print("length of fruits: " + str(len(fruits)))

    return


def accessing_tuples(**kwargs):
    log_trace("accessing_tuples")

    print("")
    print("-- positive indexing")

    # Syntax
    tpl = ('item1', 'item2', 'item3')
    first_item = tpl[0]
    second_item = tpl[1]
    fruits = ('banana', 'orange', 'mango', 'lemon')
    first_fruit = fruits[0]
    print("first_fruit: " + first_fruit)
    second_fruit = fruits[1]
    print("second_fruit: " + second_fruit)
    last_index = len(fruits) - 1
    last_fruit = fruits[last_index]
    print("last_fruit: " + last_fruit)

    print("")
    print("-- negative indexing")
    # Syntax
    tpl = ('item1', 'item2', 'item3', 'item4')
    first_item = tpl[-4]
    second_item = tpl[-3]
    fruits = ('banana', 'orange', 'mango', 'lemon')
    first_fruit = fruits[-4]
    print("first_fruit: " + first_fruit)
    second_fruit = fruits[-3]
    print("second_fruit: " + second_fruit)
    last_fruit = fruits[-1]
    print("last_fruit: " + last_fruit)

    return


def slicing_tuples(**kwargs):
    log_trace("slicing_tuples")

    print("")
    print("-- range of positive numbers")
    tpl = ('item1', 'item2', 'item3', 'item4')
    all_items = tpl[0:4]  # all items
    print (all_items)
    all_items = tpl[0:]  # all items
    print(all_items)
    middle_two_items = tpl[1:3]  # does not include item at index 3
    print (middle_two_items)
    fruits = ('banana', 'orange', 'mango', 'lemon')
    all_fruits = fruits[0:4]  # all items
    print (all_fruits)
    all_fruits = fruits[0:]  # all items
    print(all_fruits)
    orange_mango = fruits[1:3]  # doesn't include item at index 3
    print (orange_mango)
    orange_to_the_rest = fruits[1:]
    print (orange_to_the_rest)

    print("")
    print("-- range of negative numbers")
    tpl = ('item1', 'item2', 'item3', 'item4')
    all_items = tpl[-4:]  # all items
    print (all_items)
    middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
    print (middle_two_items)
    fruits = ('banana', 'orange', 'mango', 'lemon')
    all_fruits = fruits[-4:]  # all items
    print (all_fruits)
    orange_mango = fruits[-3:-1]  # doesn't include item at index 3
    print(orange_mango)
    orange_to_the_rest = fruits[-3:]
    print (orange_to_the_rest)

    return


def tuple_conversion(**kwargs):
    log_trace("tuple_conversion")

    print("")
    print("-- to list")

    tpl = ('item1', 'item2', 'item3', 'item4')
    lst = list(tpl)
    print (tpl)

    print("")
    fruits_tpl = ('banana', 'orange', 'mango', 'lemon')
    print(fruits_tpl)
    fruits_list = list(fruits_tpl)
    print(fruits_list)
    fruits_list[0] = 'apple'
    print(fruits_list)  # ['apple', 'orange', 'mango', 'lemon']

    print("")
    print("-- list to tuple")

    fruits_tpl2 = tuple(fruits_list)
    print(fruits_tpl2)  # ('apple', 'orange', 'mango', 'lemon')

    return


def checking_item_in_tuple(**kwargs):
    log_trace("checking_item_in_tuple")

    tpl = ('item1', 'item2', 'item3', 'item4')
    print('item2' in tpl)  # True

    fruits = ('banana', 'orange', 'mango', 'lemon')
    print('orange' in fruits)  # True
    print('apple' in fruits)  # False
    #fruits[0] = 'apple'  # TypeError: 'tuple' object does not support item assignment

    return


def joining_tuples(**kwargs):
    log_trace("joining_tuples")
    tpl1 = ('item1', 'item2', 'item3')
    tpl2 = ('item4', 'item5', 'item6')
    tpl3 = tpl1 + tpl2
    print (tpl3)

    fruits = ('banana', 'orange', 'mango', 'lemon')
    vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
    fruits_and_vegetables = fruits + vegetables
    print(fruits_and_vegetables)

    return

def deleting_tuples(**kwargs):
    log_trace("deleting_tuples")

    # It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
    tpl1 = ('item1', 'item2', 'item3')
    del tpl1

    fruits = ('banana', 'orange', 'mango', 'lemon')
    del fruits

    return



# ========================= main
tuples_basics()
accessing_tuples()
slicing_tuples()
tuple_conversion()
checking_item_in_tuple()
joining_tuples()
deleting_tuples()


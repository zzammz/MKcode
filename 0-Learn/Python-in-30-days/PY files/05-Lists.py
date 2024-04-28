

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



def lists_basics():
    log_trace("lists_basics")

    log_trace2("create")

    empty_list = list()  # this is an empty list, no item in the list
    print ("length of empty list")
    print(len(empty_list))  # 0

    log_trace2("initial values")
    fruits = ['banana', 'orange', 'mango', 'lemon']  # list of fruits
    vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']  # list of vegetables
    animal_products = ['milk', 'meat', 'butter', 'yoghurt']  # list of animal products
    web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']  # list of web technologies
    countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
    lst_of_diff_things = ['Jim', 250, True, {'country': 'US', 'city': 'Scranton'}]  # list containing different data types

    # Print the lists and its length
    print('Fruits:', fruits)
    print('Number of fruits:', len(fruits))
    print('Vegetables:', vegetables)
    print('Number of vegetables:', len(vegetables))
    print('Animal products:', animal_products)
    print('Number of animal products:', len(animal_products))
    print('Web technologies:', web_techs)
    print('Number of web technologies:', len(web_techs))
    print('Countries:', countries)
    print('Number of countries:', len(countries))
    print("lst_of_diff_things: ", lst_of_diff_things)
    print ('Number of items in lst_of_diff_things: ', len(lst_of_diff_things))

    log_trace2("accessing using positive indexing")
    fruits = ['banana', 'orange', 'mango', 'lemon']
    first_fruit = fruits[0]  # we are accessing the first item using its index
    print(first_fruit)  # banana
    second_fruit = fruits[1]
    print(second_fruit)  # orange
    last_fruit = fruits[3]
    print(last_fruit)  # lemon
    # Last index
    last_index = len(fruits) - 1
    last_fruit = fruits[last_index]

    log_trace2("accessing using negative indexing")
    fruits = ['banana', 'orange', 'mango', 'lemon']
    first_fruit = fruits[-4]
    last_fruit = fruits[-1]
    second_last = fruits[-2]
    print(first_fruit)  # banana
    print(last_fruit)  # lemon
    print(second_last)  # mango

    print ("first fruit via negative indexing: " + fruits [len(fruits) * -1 ]  )
    itmp = len(fruits) * -1
    print (itmp)

    return


def unpack_2():
    log_trace("unpack_2")

    lst = ['item1', 'item2', 'item3', 'item4', 'item5']
    first_item, second_item, third_item, fourth_item, fifth_item = lst
    print (lst)
    print ("first item: " + first_item)
    print("fifth item: " + fifth_item)

    #item1, item2, *other_items = lst   #

    #print(item1)
    #print(item2)
    #print(other_items)

    #myList = [1, 2, 3, 3, 4, 4, 5, 6]
    #mySet = {*myList}
    #print("The list is:")
    #print(myList)
    #print("The set is:")
    #print(mySet)

    return


def unpacking_lists():
    log_trace("unpacking_lists")

    lst = ['item1', 'item2', 'item3', 'item4', 'item5']
    #first_item, second_item, third_item, *rest = lst  ## recover
    print(first_item)  # item1
    print(second_item)  # item2
    print(third_item)  # item3
    print(rest)  # ['item4', 'item5']

    # First Example
    fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
    #first_fruit, second_fruit, third_fruit, *rest = fruits  ## recover
    print(first_fruit)  # banana
    print(second_fruit)  # orange
    print(third_fruit)  # mango
    print(rest)  # ['lemon','lime','apple']

    # Second Example about unpacking list
    #first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #
    print(first)  # 1
    print(second)  # 2
    print(third)  # 3
    print(rest)  # [4,5,6,7,8,9]
    print(tenth)  # 10

    # Third Example about unpacking list
    countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
    #gr, fr, bg, sw, *scandic, es = countries  ## recover
    print(gr)
    print(fr)
    print(bg)
    print(sw)
    print(scandic)
    print(es)

    return


def slicing_lists():
    log_trace("slicing_lists")

    log_trace2("positive indexing")
    fruits = ['banana', 'orange', 'mango', 'lemon']  # list of fruits
    vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']  # list of vegetables
    animal_products = ['milk', 'meat', 'butter', 'yoghurt']  # list of animal products
    web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']  # list of web technologies
    countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

    fruits = ['banana', 'orange', 'mango', 'lemon']
    all_fruits = fruits[0:4]  # it returns all the fruits
    # this will also give the same result as the one above
    all_fruits = fruits[0:]  # if we don't set where to stop it takes all the rest
    orange_and_mango = fruits[1:3]  # it does not include the first index
    orange_mango_lemon = fruits[1:]
    orange_and_lemon = fruits[::2]  # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

    log_trace2("negative indexing")
    fruits = ['banana', 'orange', 'mango', 'lemon']
    print ("fruits list:")
    print (fruits)
    all_fruits = fruits[-4:]  # it returns all the fruits
    orange_and_mango = fruits[-3:-1]  # it does not include the last index,['orange', 'mango']
    orange_mango_lemon = fruits[-3:]  # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
    reverse_fruits = fruits[::-1]  # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
    print ("revsersing the list")
    print (reverse_fruits)
    print (fruits[::-1])

    return


def modifying_lists():
    log_trace("modifying_lists")

    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits[0] = 'avocado'
    print(fruits)  # ['avocado', 'orange', 'mango', 'lemon']
    fruits[1] = 'apple'
    print(fruits)  # ['avocado', 'apple', 'mango', 'lemon']
    last_index = len(fruits) - 1
    fruits[last_index] = 'lime'
    print(fruits)  # ['avocado', 'apple', 'mango', 'lime']

    return


def adding_to_lists():
    #log_trace("condition_and_local_operators")
    log_trace("adding_to_lists")

    log_trace2("appending")
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.append('apple')
    print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'apple']
    fruits.append('lime')  # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
    print(fruits)

    log_trace2("inserting")
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.insert(2, 'apple')  # insert apple between orange and mango
    print(fruits)  # ['banana', 'orange', 'apple', 'mango', 'lemon']
    fruits.insert(3, 'lime')  # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
    print(fruits)

    return


def removing_from_list():
    log_trace("removing_from_list")

    index = 0
    log_trace2("using remove")
    fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
    fruits.remove('banana')
    print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
    fruits.remove('lemon')
    print(fruits)  # ['orange', 'mango', 'banana']

    log_trace2("using pop")
    lst = ['item1', 'item2']
    print(lst)
    lst.pop()  # last item
    print (lst)
    lst.pop(index)
    print(lst)

    print("")
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.pop()
    print(fruits)  # ['banana', 'orange', 'mango']

    fruits.pop(0)
    print(fruits)  # ['orange', 'mango']

    log_trace2("using del")
    lst = ['item1', 'item2']
    del lst[index]  # only a single item
    del lst  # to delete the list completely

    fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
    del fruits[0]
    print(fruits)  # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
    del fruits[1]
    print(fruits)  # ['orange', 'lemon', 'kiwi', 'lime']
    del fruits[1:3]  # this deletes items between given indexes, so it does not delete the item with index 3!
    print(fruits)  # ['orange', 'lime']
    del fruits
    #print(fruits)  # This should give: NameError: name 'fruits' is not defined

    log_trace2("clear list with del")
    mylist = ["1", "2", "3", "4", "5"]
    print(mylist)
    del mylist[0:]
    print(mylist)

    del mylist
    #print (mylist)  #this will give an error because the mylist does not exist anymore

    return


def clearing_a_list():
    log_trace("clearing_a_list")

    lst = ['item1', 'item2']
    #lst.clear()
    fruits = ['banana', 'orange', 'mango', 'lemon']
    #fruits.clear()
    #fruits.clear()
    print(fruits)  # []

    log_trace2("clear list with del")
    mylist = ["1", "2", "3", "4", "5"]
    print(mylist)
    del mylist[0:]
    print(mylist)

    return

def copying_a_list():
    log_trace("copying_a_list")

    lst = ['item1', 'item2']
    #lst_copy = lst.copy()

    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits_copy = fruits.copy()
    print(fruits_copy)  # ['banana', 'orange', 'mango', 'lemon']

    return


def joining_a_list():
    log_trace("joining_a_list")

    log_trace2("using +")
    positive_numbers = [1, 2, 3, 4, 5]
    zero = [0]
    negative_numbers = [-5, -4, -3, -2, -1]
    integers = negative_numbers + zero + positive_numbers
    print(integers)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    fruits = ['banana', 'orange', 'mango', 'lemon']
    vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
    fruits_and_vegetables = fruits + vegetables
    print(fruits_and_vegetables)  # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

    log_trace2("using extend()")

    list1 = ['item1', 'item2']
    list2 = ['item3', 'item4', 'item5']
    list1.extend(list2)

    num1 = [0, 1, 2, 3]
    num2 = [4, 5, 6]
    num1.extend(num2)
    print('Numbers:', num1)  # Numbers: [0, 1, 2, 3, 4, 5, 6]
    negative_numbers = [-5, -4, -3, -2, -1]
    positive_numbers = [1, 2, 3, 4, 5]
    zero = [0]

    negative_numbers.extend(zero)
    negative_numbers.extend(positive_numbers)
    print('Integers:', negative_numbers)  # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    fruits = ['banana', 'orange', 'mango', 'lemon']
    vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
    fruits.extend(vegetables)
    print('Fruits and vegetables:', fruits)  # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

    return


def copying_items_in_a_list():
    log_trace("copying_items_in_a_list")

    item = 0
    lst = ['item1', 'item2']
    lst.count(item)
    print (lst)
    print("items in lst: " + str(len(lst)))

    print("")
    fruits = ['banana', 'orange', 'mango', 'orange', 'lemon']
    print (fruits)
    print("count of 'orange' in fruits: " + str(fruits.count('orange')))  # 1
    print("")
    ages = [22, 19, 24, 25, 26, 24, 25, 24]
    print (ages)
    print("count of time 'ages' has 24: " + str(ages.count(24)))

    return


def find_in_list(mylist, find_value):
    find_pos = -1
    if find_value in mylist:
        find_pos = mylist.index(find_value)
    return find_pos


def finding_index_of_an_item():
    log_trace("finding_index_of_an_item")

    fruits = ['banana', 'orange', 'mango', 'lemon']
    print (fruits)
    find_value = "orange"
    print("index of " + find_value + " : " + str(find_in_list(fruits, find_value)) )
    #if find_value in fruits:
    #    print("index of " + find_value + " : " + str(fruits.index(find_value)))
    #else:
    #    print("index of " + find_value + " : not found")

    #print("index of orange: " + str(fruits.index('orange')))  # 1
    find_value = "cherry"
    print("index of " + find_value + " : " + str(find_in_list(fruits, find_value)))

    print("")
    ages = [22, 19, 24, 25, 26, 24, 25, 24]
    print (ages)
    find_value = 24
    print("index of " + str(find_value) + " : " + str(find_in_list(ages, find_value)))

    return


def sorting_a_list():
    log_trace("sorting_a_list")

    log_trace2("using sort()")
    lst = ['item1', 'item2']
    lst.sort()  # ascending
    print(lst)
    lst.sort(reverse=True)  # descending
    print(lst)

    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.sort()
    print(fruits)  # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
    fruits.sort(reverse=True)
    print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
    ages = [22, 19, 24, 25, 26, 24, 25, 24]
    ages.sort()
    print(ages)  # [19, 22, 24, 24, 24, 25, 25, 26]

    ages.sort(reverse=True)
    print(ages)  # [26, 25, 25, 24, 24, 24, 22, 19]

    log_trace2("using sorted(), which returns the ordered list without modifying the original list")
    fruits = ['banana', 'orange', 'mango', 'lemon']
    print(sorted(fruits))  # ['banana', 'lemon', 'mango', 'orange']
    print(fruits)
    print ("")
    # Reverse order
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits = sorted(fruits, reverse=True)
    print(fruits)  # ['orange', 'mango', 'lemon', 'banana']

    return


def reversing_a_list():
    log_trace("reversing_a_list")

    lst = ['item1', 'item2']
    lst.reverse()
    print(lst)

    fruits = ['banana', 'orange', 'mango', 'lemon']
    print (fruits)
    fruits.reverse()
    print(fruits)  # ['lemon', 'mango', 'orange', 'banana']
    ages = [22, 19, 24, 25, 26, 24, 25, 24]
    print (ages)
    ages.reverse()
    print(ages)  # [24, 25, 24, 26, 25, 24, 19, 22]

    return

# ========================= main

lists_basics()
unpack_2()
#unpacking_lists()
slicing_lists()
modifying_lists()
adding_to_lists()
removing_from_list()
clearing_a_list()
copying_a_list()
joining_a_list()
copying_items_in_a_list()
finding_index_of_an_item()
sorting_a_list()
reversing_a_list()



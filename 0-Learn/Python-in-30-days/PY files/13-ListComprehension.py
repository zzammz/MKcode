

import inspect
import sys

# ========================= common
def log_trace(func_name):
    print ("\n----- " + func_name + "() -----")
    return


def list_comprehension_basics():
    log_trace("list_comprehension_basics")

    print ("")
    print ("-- one way")

    # One way
    language = 'Python'
    lst = list(language)  # changing the string to list
    print(type(lst))  # list
    print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

    # Second way: list comprehension
    print("")
    print("-- second way")
    lst = [i for i in language]
    print(type(lst))  # list
    print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

    # Generating numbers
    print("")
    print("-- generate a list of numbers")

    numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
    print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # It is possible to do mathematical operations during iteration
    squares = [i * i for i in range(11)]
    print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # It is also possible to make a list of tuples
    numbers = [(i, i * i) for i in range(11)]
    print(numbers)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

    print("")
    print("-- combined with if expression")

    # Generating even numbers
    even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
    print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    # Generating odd numbers
    odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
    print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    # Filter numbers: let's filter out positive even numbers from the list below
    numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
    positives_from_numbers = [i for i in numbers if i > 0]
    print (positives_from_numbers)
    positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
    print(positive_even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    # Flattening a three dimensional array
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_list = [number for row in list_of_lists for number in row]
    print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

    return


def lambda_function():
    log_trace("lambda_function")

    print("")
    print("-- creating")

    x = lambda param1, param2, param3: param1 + param2 + param2
    #print(x(arg1, arg2, arg3))

    # Named function
    def add_two_nums(a, b):
        return a + b

    print(add_two_nums(2, 3))  # 5
    # Lets change the above function to a lambda function
    add_two_nums = lambda a, b: a + b
    print(add_two_nums(2, 3))  # 5

    # Self invoking lambda function
    (lambda a, b: a + b)(2, 3)  # 5 - need to encapsulate it in print() to see the result in the console

    square = lambda x: x ** 2
    print(square(3))  # 9
    cube = lambda x: x ** 3
    print(cube(3))  # 27

    # Multiple variables
    multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
    print(multiple_variable(5, 5, 3))  # 22

    print("")
    print("-- lambda function inside another function")

    def power(x):
        return lambda n: x ** n

    cube = power(2)(3)  # function power now need 2 arguments to run, in separate rounded brackets
    print(cube)  # 8
    two_power_of_five = power(2)(5)
    print(two_power_of_five)  # 32

    return


# ========================= main
list_comprehension_basics()
lambda_function()


